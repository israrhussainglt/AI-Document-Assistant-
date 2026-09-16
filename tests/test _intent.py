from backend.agent.intent_detector import detect_intent


print("Testing intent detection...")

queries = [
    "What is database normalization?",
    "Summarize this document",
    "Find all the books mentioned in the document"
]

for query in queries:
    intent = detect_intent(query)

    print("\nQuestion:", query)
    print("Intent:", intent)