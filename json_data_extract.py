import json
from pathlib import Path

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

if isinstance(data, dict):
    print("Top-level keys:", list(data.keys()))

name = data.get("name")
friends = data.get("friends")

Response = ", ".join(map(str, friends))

print(Response)
# print(data)