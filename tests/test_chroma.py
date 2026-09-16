from backend.services.vector_store import collection


print("Collection:", collection.name)
print("Number of documents:", collection.count())

print("\nStored data:")
print(collection.get())