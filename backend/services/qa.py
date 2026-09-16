import cohere

from backend.config import COHERE_API_KEY
from backend.services.retriever import search_documents


client = cohere.ClientV2(api_key=COHERE_API_KEY)


def answer_question(
    question: str,
    document_name: str,
    conversation_history: list
):

    # Search for relevant information
    results = search_documents(
        question,
        top_k=5
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # Filter results to the selected document
    filtered_documents = []
    filtered_metadatas = []

    for document, metadata in zip(documents, metadatas):

        if metadata["document"] == document_name:
            filtered_documents.append(document)
            filtered_metadatas.append(metadata)

    # If no matching chunks are found
    if not filtered_documents:
        return {
            "answer": "I could not find this information in the selected document.",
            "sources": []
        }

    # Build document context
    context_parts = []

    for document, metadata in zip(
        filtered_documents,
        filtered_metadatas
    ):

        context_parts.append(
            f"Document: {metadata['document']}\n"
            f"Page: {metadata['page']}\n"
            f"Content: {document}"
        )

    context = "\n\n".join(context_parts)

    # Build conversation history
    history_text = ""

    for message in conversation_history:

        history_text += (
            f"{message['role'].capitalize()}: "
            f"{message['content']}\n"
        )

    prompt = f"""
You are an AI Document Intelligence Agent.

Answer the user's question using ONLY the selected document
context and the conversation history.

Selected document:
{document_name}

Conversation history:
{history_text}

Document context:
{context}

Rules:
- Use the conversation history to understand follow-up questions.
- Use only information from the selected document.
- Do not use information from other documents.
- Do not invent information.
- If the answer cannot be found in the selected document, say:
"I could not find this information in the selected document."

Current user question:
{question}
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

    answer = response.message.content[0].text

    # Create unique sources
    sources = []
    seen = set()

    for metadata in filtered_metadatas:

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
        "answer": answer,
        "sources": sources
    }