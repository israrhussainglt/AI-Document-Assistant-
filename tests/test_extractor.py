from backend.services.extractor import extract_information


print("Testing information extraction...")

result = extract_information(
    "12_databases.pdf",
    "all books mentioned in the document"
)

print("\nExtracted Information:")
print(result["result"])

print("\nSources:")
print(result["sources"])