from app.catalog_loader import CatalogLoader


class KeywordRetriever:
    def __init__(self, assessments):
        self.assessments = assessments

    def search(self, query):
        query = query.lower()

        results = []

        for assessment in self.assessments:
            searchable_text = (
                assessment.name + " " +
                assessment.description + " " +
                " ".join(assessment.keys)
            ).lower()

            if query in searchable_text:
                results.append(assessment)

        return results


if __name__ == "__main__":
    loader = CatalogLoader()

    assessments = loader.load_catalog()

    retriever = KeywordRetriever(assessments)

    results = retriever.search("java")

    print(f"Found {len(results)} assessments\n")

    for assessment in results[:10]:
        print(assessment.name)