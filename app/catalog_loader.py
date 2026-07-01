import json
from pathlib import Path

from app.models import Assessment


class CatalogLoader:
    def __init__(self, catalog_path="data/shl_catalog.json"):
        self.catalog_path = Path(catalog_path)
        self.catalog = []

    def load_catalog(self):
        with open(self.catalog_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.catalog = [
            Assessment(
                entity_id=item.get("entity_id", ""),
                name=item.get("name", ""),
                link=item.get("link", ""),
                description=item.get("description", ""),
                duration=item.get("duration", ""),
                remote=item.get("remote", ""),
                adaptive=item.get("adaptive", ""),
                job_levels=item.get("job_levels", []),
                languages=item.get("languages", []),
                keys=item.get("keys", []),
            )
            for item in data
        ]

        return self.catalog


if __name__ == "__main__":
    loader = CatalogLoader()

    assessments = loader.load_catalog()

    print(f"Loaded {len(assessments)} assessments")