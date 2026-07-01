from app.retriever import KeywordRetriever
from app.embeddings import EmbeddingRetriever


class HybridRetriever:

    def __init__(self, assessments):
        self.keyword = KeywordRetriever(assessments)
        self.semantic = EmbeddingRetriever(assessments)

    def search(self, query, top_k=10):

        keyword_results = self.keyword.search(query)
        semantic_results = self.semantic.search(query, top_k)

        scores = {}

        for assessment in keyword_results:
            scores[assessment.entity_id] = {
                "assessment": assessment,
                "score": 2,
            }

        for assessment in semantic_results:

            if assessment.entity_id in scores:
                scores[assessment.entity_id]["score"] += 1
            else:
                scores[assessment.entity_id] = {
                    "assessment": assessment,
                    "score": 1,
                }

        ranked = sorted(
            scores.values(),
            key=lambda x: x["score"],
            reverse=True,
        )

        return [
            item["assessment"]
            for item in ranked[:top_k]
        ]