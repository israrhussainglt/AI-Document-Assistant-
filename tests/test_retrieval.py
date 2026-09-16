from backend.services.retriever import search_documents


print("Searching documents...")

results = search_documents(
    "What is machine learning?"
)

print("Search completed.")
print(results)