#!/usr/bin/env python3
"""Append emoji (or gaps) to Shared/Catalog.json from a user-supplied list.

Each line:

    category-id/subcategory-id | emoji-or-empty | Display name | keyword, keyword

Examples:

    travel/air-travel | ✈️ | Passenger jet | airplane, jet, plane
    geography/geology | | Trilobite | cambrian, fossil

Then rebuild the Geomoji scheme in Xcode. Optionally run
`python3 scripts/generate_catalog.py` only if you are editing the Python
taxonomy; that command overwrites Catalog.json from scripts/generate_catalog.py.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "Shared" / "Catalog.json"


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "item"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("list_file", help="UTF-8 text file of pipe-separated rows")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    categories = {c["id"]: c for c in catalog["categories"]}
    existing = {
        item["id"]
        for category in catalog["categories"]
        for subcategory in category["subcategories"]
        for item in subcategory["items"]
    }

    added = 0
    for raw in Path(args.list_file).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            print(f"skip (need at least 3 columns): {line}", file=sys.stderr)
            continue
        path, emoji, name = parts[0], parts[1], parts[2]
        keywords = [k.strip() for k in parts[3].split(",")] if len(parts) > 3 and parts[3] else []
        if "/" not in path:
            print(f"skip (category/subcategory required): {line}", file=sys.stderr)
            continue
        cat_id, sub_id = path.split("/", 1)
        if cat_id not in categories:
            print(f"skip unknown category {cat_id}", file=sys.stderr)
            continue
        subcategory = next((s for s in categories[cat_id]["subcategories"] if s["id"] == sub_id), None)
        if subcategory is None:
            print(f"skip unknown subcategory {cat_id}/{sub_id}", file=sys.stderr)
            continue
        item_id = slug(name)
        suffix = 2
        while item_id in existing:
            item_id = f"{slug(name)}-{suffix}"
            suffix += 1
        entry = {"id": item_id, "name": name, "keywords": keywords}
        if emoji:
            entry["emoji"] = emoji
        else:
            entry["gap"] = True
        subcategory["items"].append(entry)
        existing.add(item_id)
        added += 1
        print(f"added {cat_id}/{sub_id}/{item_id}")

    if added:
        real = gaps = 0
        for category in catalog["categories"]:
            for subcategory in category["subcategories"]:
                for item in subcategory["items"]:
                    if item.get("gap") or not item.get("emoji"):
                        gaps += 1
                    else:
                        real += 1
        catalog["stats"] = {"emoji": real, "gaps": gaps, "total": real + gaps}
        CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Added {added} item(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
