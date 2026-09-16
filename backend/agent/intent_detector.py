import cohere

from backend.config import COHERE_API_KEY


client = cohere.ClientV2(api_key=COHERE_API_KEY)


def detect_intent(user_query: str):

    prompt = f"""
Classify the user's request into exactly one of these intents:

- question
- summarize
- extract

User request:
{user_query}

Return only the intent name.
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

    intent = response.message.content[0].text.strip().lower()

    if intent not in ["question", "summarize", "extract"]:
        intent = "question"

    return intent