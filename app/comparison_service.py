from app.catalog_loader import CatalogLoader
from app.gemini_client import ask_gemini


class ComparisonService:
    """
    Handles comparison between two SHL assessments.
    """

    def __init__(self):
        loader = CatalogLoader()
        self.assessments = loader.load_catalog()

    def find_assessment(self, name: str):
        aliases = {
            "gsa": ["global skills", "global skills development report"],
            "opq": ["opq", "occupational personality questionnaire"],
        }

        search_terms = aliases.get(name.lower(), [name.lower()])

        for assessment in self.assessments:
            assessment_name = assessment.name.lower()

            for term in search_terms:
                if term in assessment_name:
                    return assessment

        return None

    def compare(self, first: str, second: str):
        assessment1 = self.find_assessment(first)
        assessment2 = self.find_assessment(second)

        if not assessment1 or not assessment2:
            return "Sorry, I couldn't find one or both assessments."

        prompt = f"""
You are an SHL assessment expert.

Compare these two assessments.

Assessment 1:
Name: {assessment1.name}
Description: {assessment1.description}

Assessment 2:
Name: {assessment2.name}
Description: {assessment2.description}

Explain:

1. Purpose
2. Key differences
3. When to use each
4. Keep the answer under 250 words.
"""

        return ask_gemini(prompt)


if __name__ == "__main__":
    service = ComparisonService()

    comparison = service.compare("OPQ", "GSA")

    print(comparison)