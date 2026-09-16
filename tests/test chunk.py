from backend.services.chunker import chunk_text


text = """
Artificial Intelligence is transforming many industries.
Machine learning allows computers to learn from data.
Generative AI can create text, images, and other content.
Retrieval Augmented Generation allows AI systems to use external documents.
"""


chunks = chunk_text(text, chunk_size=100, overlap=20)


for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)