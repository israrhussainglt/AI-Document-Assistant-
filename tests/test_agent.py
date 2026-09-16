from backend.agent.agent import run_agent


document = "12_databases.pdf"


print("=" * 50)
print("QUESTION 1")
print("=" * 50)

result = run_agent(
    "What is database normalization?",
    document
)

print("Intent:", result["intent"])
print("Answer:", result["answer"])
print("Sources:", result["sources"])


print("\n" + "=" * 50)
print("QUESTION 2")
print("=" * 50)

result = run_agent(
    "Why is it important?",
    document
)

print("Intent:", result["intent"])
print("Answer:", result["answer"])
print("Sources:", result["sources"])


print("\n" + "=" * 50)
print("CONVERSATION HISTORY")
print("=" * 50)

for message in result["history"]:
    print(message)