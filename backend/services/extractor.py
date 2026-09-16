import cohere

from backend.config import COHERE_API_KEY
from backend.services.vector_store import collection


client = cohere.ClientV2(api_key=COHERE_API_KEY)


def extract_information(document_name: str, information_type: str):

    results = collection.get(
        where={"document": document_name}
    )

    documents = results["documents"]

    if not documents:
        return {
            "result": "Document not found.",
            "sources": []
        }

    full_text = "\n\n".join(documents)

    prompt = f"""
Extract the requested information from the document.

Information to extract:
{information_type}

Rules:
- Use only the provided document.
- Return the extracted information as a clear numbered list.
- Do not invent information.
- If the information is not found, say "No information found."

Document:
{full_text}
"""

    response = client.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.message.content[0].text

    # Create unique document/page sources
    metadatas = results["metadatas"]

    sources = []
    seen = set()

    for metadata in metadatas:
        key = (
            metadata["document"],
            metadata["page"]
        )

        if key not in seen:
            seen.add(key)

            sources.append({
                "document": metadata["document"],
                "page": metadata["page"]
            })

    return {
        "result": result,
        "sources": sources
    }