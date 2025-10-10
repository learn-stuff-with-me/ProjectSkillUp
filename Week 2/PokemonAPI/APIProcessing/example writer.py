from pathlib import *
import json


data = {
    "One": "test",
    "two": "test2",
}

file_path = Path.home() / "subdirectory" / "example.json"

print(file_path.parent)

file_path.parent.mkdir(parents=True, exist_ok=True)

with file_path.open("w") as f:
    json.dump(data, f)
