import os
import traceback

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.services.pdf_processor import extract_text_from_pdf
from backend.services.chunker import chunk_text
from backend.services.embeddings import create_embedding
from backend.services.vector_store import add_document


router = APIRouter()

UPLOAD_DIR = "data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        pages = extract_text_from_pdf(file_path)

        all_chunks = []

        for page in pages:

            chunks = chunk_text(
                page["text"],
                chunk_size=100,
                overlap=20
            )

            for chunk in chunks:

                embedding = create_embedding(chunk)

                add_document(
                    document=file.filename,
                    page=page["page"],
                    text=chunk,
                    embedding=embedding
                )

                all_chunks.append({
                    "document": file.filename,
                    "page": page["page"],
                    "text": chunk
                })

        return {
            "filename": file.filename,
            "pages": len(pages),
            "chunks": len(all_chunks),
            "message": "PDF processed and stored in ChromaDB successfully."
        }
    except Exception as e:
        print(f"Error processing upload: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=f"Error processing PDF: {str(e)}"
        )