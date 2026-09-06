#!/usr/bin/env python3
"""Validate Shared/Catalog.json: unique ids, required taxonomy, emoji vs gaps."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "Shared" / "Catalog.json"

REQUIRED_CATEGORIES = {
    "travel": ["air-travel", "road-trips", "cruises", "international", "luggage", "lodging"],
    "geography": ["landforms", "maps", "weather", "geology", "oceans"],
    "outdoors": ["hiking", "camping", "climbing", "paddling", "cycling"],
    "hunting": ["big-game", "deer", "waterfowl", "turkey", "upland", "hunting-equipment"],
    "fishing": ["freshwater", "saltwater", "fly-fishing", "fish-species", "fishing-equipment"],
    "wildlife": ["mammals", "birds", "wildlife-fish", "reptiles"],
    "places": ["national-parks", "states", "countries", "destinations"],
}

REQUIRED_MAPPINGS = {
    "passenger-jet": "✈️",
    "suitcase": "🧳",
    "compass": "🧭",
    "whitetail": "🦌",
    "duck": "🦆",
}


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    categories = {c["id"]: c for c in data["categories"]}
    errors: list[str] = []

    for cat_id, subs in REQUIRED_CATEGORIES.items():
        if cat_id not in categories:
            errors.append(f"missing category {cat_id}")
            continue
        have = {s["id"] for s in categories[cat_id]["subcategories"]}
        for sub_id in subs:
            if sub_id not in have:
                errors.append(f"missing subcategory {cat_id}/{sub_id}")

    ids: list[str] = []
    emoji_ids: dict[str, str] = {}
    real = gaps = 0
    for category in data["categories"]:
        for subcategory in category["subcategories"]:
            for item in subcategory["items"]:
                ids.append(item["id"])
                if item.get("gap") or not item.get("emoji"):
                    gaps += 1
                    if item.get("emoji"):
                        errors.append(f"{item['id']} is a gap but still has emoji")
                else:
                    real += 1
                    emoji_ids[item["id"]] = item["emoji"]
                    if not isinstance(item["emoji"], str) or not item["emoji"].strip():
                        errors.append(f"{item['id']} has empty emoji")

    dupes = [i for i, n in Counter(ids).items() if n > 1]
    if dupes:
        errors.append(f"duplicate ids: {dupes}")

    for item_id, glyph in REQUIRED_MAPPINGS.items():
        if emoji_ids.get(item_id) != glyph:
            errors.append(f"{item_id} should map to {glyph}, got {emoji_ids.get(item_id)!r}")

    print(f"Categories: {len(data['categories'])}")
    print(f"Unicode emoji: {real}")
    print(f"Gaps: {gaps}")
    print(f"Total items: {real + gaps}")
    if errors:
        print("FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
