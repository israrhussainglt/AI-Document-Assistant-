import cohere

from backend.config import COHERE_API_KEY
from backend.services.vector_store import collection


client = cohere.ClientV2(api_key=COHERE_API_KEY)


def summarize_document(document_name: str):

    results = collection.get(
        where={"document": document_name}
    )

    documents = results["documents"]

    if not documents:
        return {
            "summary": "Document not found.",
            "sources": []
        }

    full_text = "\n\n".join(documents)

    prompt = f"""
Summarize the following document.

Provide:
1. A short overall summary
2. Main topics
3. Important points
4. Key conclusion

Use only the provided document content.

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

    summary = response.message.content[0].text

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
        "summary": summary,
        "sources": sources
    }