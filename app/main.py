from fastapi import FastAPI

from app.models import ChatRequest, ChatResponse
from app.conversation_manager import ConversationManager
from app.chatbot_service import ChatbotService

app = FastAPI()

manager = ConversationManager()
chatbot = ChatbotService()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    messages = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in request.messages
    ]

    latest_message = messages[-1]["content"]

    intent = manager.detect_intent(messages)

    # Recommendation
    if intent == "recommend":
        result = chatbot.recommend(latest_message)
        return ChatResponse(**result)

    # Comparison (placeholder)
    elif intent == "compare":
        return ChatResponse(
            reply="Comparison feature will be implemented next.",
            recommendations=[],
            end_of_conversation=False,
        )

    # Clarification
    elif intent == "clarify":
        return ChatResponse(
            reply="Could you tell me which role you're hiring for?",
            recommendations=[],
            end_of_conversation=False,
        )

    # Refuse
    else:
        return ChatResponse(
            reply="I'm an SHL Assessment Assistant. I can help you recommend and compare SHL assessments, but I can't answer unrelated questions.",
            recommendations=[],
            end_of_conversation=True,
        )