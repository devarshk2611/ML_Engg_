"""
file_ops.py
Utilities for reading/writing TXT, CSV, and JSON files.
Run directly to see examples create files under ./data/.
"""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def write_text(path, text):
    Path(path).write_text(text, encoding="utf-8")

def read_text(path):
    return Path(path).read_text(encoding="utf-8")

def write_csv(path, rows, header=None):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)

def read_csv(path):
    with open(path, "r", newline="", encoding="utf-8") as f:
        return list(csv.reader(f))

def write_json(path, obj, indent=2):
    Path(path).write_text(json.dumps(obj, indent=indent), encoding="utf-8")

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    txt_path = DATA_DIR / "hello.txt"
    csv_path = DATA_DIR / "people.csv"
    json_path = DATA_DIR / "config.json"

    # TXT
    write_text(txt_path, "Hello from file_ops!\nThis is a test file.")
    print("TXT read:", read_text(txt_path).splitlines())

    # CSV
    write_csv(csv_path, rows=[["Alice", 24], ["Bob", 31]], header=["name", "age"])
    print("CSV read:", read_csv(csv_path))

    # JSON
    cfg = {"env": "dev", "retries": 3, "features": ["log", "cache"]}
    write_json(json_path, cfg)
    print("JSON read:", read_json(json_path))
