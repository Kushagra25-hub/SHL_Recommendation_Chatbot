from fastapi import FastAPI

from app.models import ChatRequest, ChatResponse
from app.conversation_manager import ConversationManager
from app.chatbot_service import ChatbotService
from app.comparison_service import ComparisonService

app = FastAPI()

manager = ConversationManager()
chatbot = ChatbotService()
comparison_service = ComparisonService()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Convert request messages to dictionaries
    messages = [
        {
            "role": message.role,
            "content": message.content,
        }
        for message in request.messages
    ]

    # Combine all user messages (multi-turn support)
    user_query = " ".join(
        message["content"]
        for message in messages
        if message["role"] == "user"
    )

    # Detect intent
    intent = manager.detect_intent(messages)

    # ===========================
    # Recommendation
    # ===========================
    if intent == "recommend":
        result = chatbot.recommend(user_query)
        return ChatResponse(**result)

    # ===========================
    # Comparison
    # ===========================
    elif intent == "compare":

        query = user_query.lower().replace("compare", "").strip()

        parts = [part.strip() for part in query.split("and")]

        if len(parts) != 2:
            return ChatResponse(
                reply="Please specify two assessments to compare. Example: Compare OPQ and GSA.",
                recommendations=[],
                end_of_conversation=False,
            )

        comparison = comparison_service.compare(parts[0], parts[1])

        return ChatResponse(
            reply=comparison,
            recommendations=[],
            end_of_conversation=True,
        )

    # ===========================
    # Clarification
    # ===========================
    elif intent == "clarify":
        return ChatResponse(
            reply=(
                "Could you tell me:\n"
                "- What role are you hiring for?\n"
                "- What seniority level?\n"
                "- Any specific skills?"
            ),
            recommendations=[],
            end_of_conversation=False,
        )

    # ===========================
    # Refuse
    # ===========================
    else:
        return ChatResponse(
            reply=(
                "I'm an SHL Assessment Assistant. "
                "I can recommend and compare SHL assessments, "
                "but I can't answer unrelated questions."
            ),
            recommendations=[],
            end_of_conversation=True,
        )