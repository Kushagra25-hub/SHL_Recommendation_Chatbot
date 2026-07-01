from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


class EmbeddingRetriever:
    def __init__(self, assessments):
        self.assessments = assessments

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Creating embeddings...")

        documents = [
            f"{a.name} {a.description} {' '.join(a.keys)}"
            for a in assessments
        ]

        embeddings = self.model.encode(
            documents,
            convert_to_numpy=True
        )

        faiss.normalize_L2(embeddings)

        self.index = faiss.IndexFlatIP(
            embeddings.shape[1]
        )

        self.index.add(embeddings)

    def search(self, query, top_k=10):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.assessments[idx])

        return results
    

if __name__ == "__main__":

    from app.catalog_loader import CatalogLoader

    loader = CatalogLoader()

    assessments = loader.load_catalog()

    retriever = EmbeddingRetriever(
        assessments
    )

    results = retriever.search(
        "backend developer"
    )

    print()

    for assessment in results:
        print(assessment.name)