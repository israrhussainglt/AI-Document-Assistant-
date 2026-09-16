import chromadb


client = chromadb.PersistentClient(
    path="data/chroma"
)


collection = client.get_or_create_collection(
    name="documents"
)


def add_document(
    document: str,
    page: int,
    text: str,
    embedding: list
):
    collection.add(
        ids=[f"{document}_{page}_{hash(text)}"],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "document": document,
                "page": page
            }
        ]
    )


def get_all_documents():
    """Get list of unique documents in the collection"""
    try:
        results = collection.get()
        if not results['metadatas']:
            return []
        
        # Extract unique documents
        unique_docs = {}
        for metadata in results['metadatas']:
            doc_name = metadata.get('document')
            if doc_name and doc_name not in unique_docs:
                unique_docs[doc_name] = {
                    'filename': doc_name,
                    'pages': set()
                }
            if doc_name:
                unique_docs[doc_name]['pages'].add(metadata.get('page', 0))
        
        # Convert to list format
        documents = []
        for doc in unique_docs.values():
            documents.append({
                'filename': doc['filename'],
                'pages': len(doc['pages'])
            })
        
        return documents
    except Exception as e:
        print(f"Error getting documents: {e}")
        return []