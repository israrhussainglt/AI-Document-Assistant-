from backend.services.embeddings import create_embedding
from backend.services.vector_store import collection


def search_documents(query: str, top_k: int = 3):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

