from backend.agent.memory import ConversationMemory


print("Testing Conversation Memory...")

memory = ConversationMemory()


memory.add_message(
    "user",
    "What is database normalization?"
)

memory.add_message(
    "assistant",
    "Database normalization reduces data redundancy."
)


print("\nConversation History:")

print(memory.get_history())