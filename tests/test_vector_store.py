from backend.services.embeddings import create_embedding
from backend.services.vector_store import add_document


print("Creating embedding...")

text = "Machine learning allows computers to learn patterns from data."

embedding = create_embedding(text)

print("Embedding created.")

add_document(
    document="test.pdf",
    page=1,
    text=text,
    embedding=embedding
)

print("Document stored in ChromaDB successfully.")