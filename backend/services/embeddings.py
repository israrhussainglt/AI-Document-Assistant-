import cohere

from backend.config import COHERE_API_KEY


client = cohere.ClientV2(api_key=COHERE_API_KEY)


def create_embedding(text: str):
    response = client.embed(
        model="embed-english-v3.0",
        texts=[text],
        input_type="search_document"
    )

    return response.embeddings.float[0]