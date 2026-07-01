from difflib import SequenceMatcher


class EmbeddingRetriever:
    """
    Lightweight semantic retriever using fuzzy matching.
    No ML model required.
    """

    def __init__(self, assessments):
        self.assessments = assessments

    def search(self, query, top_k=10):

        query = query.lower()

        scored = []

        for assessment in self.assessments:

            text = (
                assessment.name
                + " "
                + assessment.description
                + " "
                + " ".join(assessment.keys)
            ).lower()

            score = SequenceMatcher(
                None,
                query,
                text,
            ).ratio()

            scored.append((score, assessment))

        scored.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return [
            assessment
            for score, assessment in scored[:top_k]
        ]


if __name__ == "__main__":

    from app.catalog_loader import CatalogLoader

    loader = CatalogLoader()

    assessments = loader.load_catalog()

    retriever = EmbeddingRetriever(assessments)

    results = retriever.search("backend developer")

    for assessment in results:
        print(assessment.name)