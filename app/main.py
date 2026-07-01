from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        reply="Hello! I'm your SHL Assessment Assistant. Tell me about the role you're hiring for.",
        recommendations=[],
        end_of_conversation=False
    )