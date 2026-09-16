from backend.services.embeddings import create_embedding


print("Starting embedding test...")

text = "Machine learning is a method of learning patterns from data."

embedding = create_embedding(text)

print("Embedding created successfully.")
print("Number of dimensions:", len(embedding))
print("First 5 values:", embedding[:5])