from backend.agent.intent_detector import detect_intent
from backend.services.qa import answer_question
from backend.services.summarizer import summarize_document
from backend.services.extractor import extract_information
from backend.agent.memory import ConversationMemory


memory = ConversationMemory()


def run_agent(user_query: str, document_name: str):

    # Get previous conversation
    conversation_history = memory.get_history()

    # Detect intent
    intent = detect_intent(user_query)

    # Save user message
    memory.add_message(
        "user",
        user_query
    )

    # Question
    if intent == "question":

        result = answer_question(
            user_query,
            document_name,
            conversation_history
        )

        answer = result["answer"]

        memory.add_message(
            "assistant",
            answer
        )

        return {
            "intent": intent,
            "answer": answer,
            "sources": result["sources"],
            "history": memory.get_history()
        }

    # Summarization
    if intent == "summarize":

        result = summarize_document(document_name)

        answer = result["summary"]

        memory.add_message(
            "assistant",
            answer
        )

        return {
            "intent": intent,
            "answer": answer,
            "sources": result["sources"],
            "history": memory.get_history()
        }

    # Information extraction
    if intent == "extract":

        result = extract_information(
            document_name,
            user_query
        )

        answer = result["result"]

        memory.add_message(
            "assistant",
            answer
        )

        return {
            "intent": intent,
            "answer": answer,
            "sources": result["sources"],
            "history": memory.get_history()
        }

    return {
        "intent": "unknown",
        "answer": "I could not understand the request.",
        "sources": [],
        "history": memory.get_history()
    }