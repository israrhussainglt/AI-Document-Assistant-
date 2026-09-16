from backend.services.summarizer import summarize_document


print("Testing document summarization...")

result = summarize_document("12_databases.pdf")

print("\nSummary:")
print(result["summary"])

print("\nSources:")
print(result["sources"])