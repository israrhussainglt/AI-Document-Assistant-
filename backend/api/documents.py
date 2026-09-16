from fastapi import APIRouter
from backend.services.vector_store import get_all_documents

router = APIRouter()


@router.get("/documents")
async def get_documents():
    """Get all uploaded documents"""
    documents = get_all_documents()
    return {
        "documents": documents
    }
