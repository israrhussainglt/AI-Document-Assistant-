from backend.services.qa import answer_question


print("Asking question...")

result = answer_question(
    "What is machine learning?"
)

print("\nAnswer:")
print(result["answer"])

print("\nSources:")
print(result["sources"])