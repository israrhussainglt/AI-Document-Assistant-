from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.agent.agent import run_agent
from backend.services.summarizer import summarize_document


router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    document_name: str


class SummarizeRequest(BaseModel):
    document_name: str


@router.post("/chat")
def chat(request: ChatRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if not request.document_name.strip():
        raise HTTPException(
            status_code=400,
            detail="Document name is required."
        )

    result = run_agent(
        request.question,
        request.document_name
    )

    return result


@router.post("/summarize")
def summarize(request: SummarizeRequest):

    if not request.document_name.strip():
        raise HTTPException(
            status_code=400,
            detail="Document name is required."
        )

    try:
        result = summarize_document(request.document_name)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error summarizing document: {str(e)}"
        )