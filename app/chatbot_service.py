from app.catalog_loader import CatalogLoader
from app.hybrid_retriever import HybridRetriever
from app.gemini_client import ask_gemini


class ChatbotService:
    def __init__(self):
        loader = CatalogLoader()
        assessments = loader.load_catalog()

        self.retriever = HybridRetriever(assessments)

    def recommend(self, user_query: str):
        """
        Recommend SHL assessments based on the user's query.
        """

        results = self.retriever.search(user_query, top_k=10)

        prompt = f"""
You are an SHL assessment recommendation assistant.

The user asked:
{user_query}

Recommend the assessments below.

Explain briefly why they fit.

Assessments:

"""

        for assessment in results:
            prompt += f"""
Name: {assessment.name}
Description: {assessment.description}
"""

        reply = ask_gemini(prompt)

        recommendations = []

        for assessment in results:
            recommendations.append(
                {
                    "name": assessment.name,
                    "url": assessment.link,
                    "test_type": ", ".join(assessment.keys),
                }
            )

        return {
            "reply": reply,
            "recommendations": recommendations,
            "end_of_conversation": True,
        }


if __name__ == "__main__":

    chatbot = ChatbotService()

    response = chatbot.recommend(
        "Hiring a Java backend developer"
    )

    print(response["reply"])

    print("\nRecommendations:\n")

    for rec in response["recommendations"][:5]:
        print(rec["name"])