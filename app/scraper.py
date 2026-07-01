import json

with open("data/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(type(catalog))
print(len(catalog))
print(catalog[0]["name"])