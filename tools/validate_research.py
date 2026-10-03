#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def load(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: {exc}")
        return {}

sources = load("research/sources.json")
index = load("research/index.json")

ids = [s.get("id") for s in sources.get("sources", [])]
if len(ids) != len(set(ids)):
    errors.append("research/sources.json: duplicate source ids")
for s in sources.get("sources", []):
    for key in ("id", "grade", "title", "url"):
        if not s.get(key):
            errors.append(f"source missing {key}: {s!r}")
    if s.get("grade") not in {"A","B","C","D"}:
        errors.append(f"invalid source grade: {s!r}")

area_ids = [a.get("id") for a in index.get("areas", [])]
if len(area_ids) != len(set(area_ids)):
    errors.append("research/index.json: duplicate area ids")
for a in index.get("areas", []):
    if a.get("status") not in {"todo","seeded","partial","complete","blocked"}:
        errors.append(f"invalid area status: {a!r}")
    if a.get("file") and not (ROOT / a["file"]).exists():
        errors.append(f"missing referenced file: {a['file']}")

if errors:
    print("\n".join("ERROR: " + e for e in errors))
    sys.exit(1)

print(f"OK: {len(ids)} sources, {len(area_ids)} research areas")
