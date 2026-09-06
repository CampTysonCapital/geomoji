# Geomoji

A local **SwiftUI iOS emoji catalog** for a geology-minded traveler: adventure, outdoors, hunting, fishing, wildlife, places, and earth science. Tap a unicode emoji to copy it. This is **not** a Messages sticker pack and not an App Store listing.

The containing app is useful on its own. An optional custom keyboard can insert the same characters into Messages or any other text field.

## Open and run

1. On a Mac, open `Geomoji.xcodeproj` in Xcode 15 or later (iOS 17 SDK).
2. Select the **Geomoji** scheme and an iPhone or iPad simulator (or a signed-in device).
3. In the Geomoji target’s Signing & Capabilities tab, choose your **Team**. The bundle IDs below are placeholders; change them if they collide with something you already own.
4. Press Run. The first launch shows seven top-level categories.

On the simulator, tap an emoji, then paste into Notes or Messages to confirm the clipboard.

## How to use the app

- **Browse** — Travel, Geography, Outdoors, Hunting, Fishing, Wildlife, Places. Each category has subcategories (Air Travel, Geology, Waterfowl, and so on).
- **Tap an emoji** — copies the real unicode character and shows a short “Copied” banner.
- **Star** — long-press (or use the star) to save **Favorites**.
- **Recents** — last ~40 emoji you copied or inserted.
- **Search** — match on display name, keywords, or the character itself (`deer`, `jet`, `compass`, `trilobite`, `Yellowstone`).
- **Gaps** — concepts with no good unicode emoji (trilobite, binoculars, treestand, mallard drake, Grand Canyon, …) appear as a dashed “No emoji yet” cell. They are catalog placeholders, not custom drawings. Hide them with the toolbar button on a category page.

## Optional keyboard

The **GeomojiKeyboard** extension is embedded in the app. It only inserts unicode text.

1. Run the app on a simulator or device at least once so the extension is installed.
2. Settings → General → Keyboard → Keyboards → **Add New Keyboard…** → **Geomoji**.
3. In any text field, hold the **globe** key and choose Geomoji.
4. The keyboard inserts emoji without **Allow Full Access**. Recents inside the keyboard are local to the extension.

To sync favorites and recents between the app and keyboard later, add an App Group (`group.com.camptysoncapital.geomoji`) to both `.entitlements` files, switch `AppConstants.sharedDefaults()` to `UserDefaults(suiteName:)`, and enable Full Access. That needs a paid developer team and is optional.

The keyboard skips gap rows. It is not a system emoji replacement and does not need to be enabled for the catalog app to be useful.

## Category map

Mapped to the closest unicode emoji where a reasonable glyph exists. Distinctive misses stay as gaps.

| Category | Subcategories | Examples |
| --- | --- | --- |
| Travel | Air Travel, Road Trips, Cruises, International, Luggage, Lodging | ✈️ 🛫 🛬 🛩️ 🧳 🧭 🏨 🛳️ 🚗 |
| Geography | Landforms, Maps, Weather, Geology, Oceans | ⛰️ 🌋 🪨 💎 🦕 🦖 🗺️ 🌡️ 🔬 |
| Outdoors | Hiking, Camping, Climbing, Paddling, Cycling | 🥾 🏕️ 🧗 🛶 🚲 🌲 🔥 |
| Hunting | Big Game, Deer, Waterfowl, Turkey, Upland, Equipment | 🦌 🦆 🪿 🦃 🐻 🫎 🏹 |
| Fishing | Freshwater, Saltwater, Fly Fishing, Species, Equipment | 🎣 🐟 🐠 🦈 🪱 |
| Wildlife | Mammals, Birds, Fish, Reptiles | 🦊 🐺 🦅 🦉 🐊 🦕 |
| Places | National Parks, States, Countries, Famous destinations | 🏞️ 🇺🇸 🗽 🗻 |

Starter geology / adventure glyphs from the original brief are in **Geography → Geology** and **Outdoors** (rock, gem, volcano, bone, dinosaurs, globes, pick, flashlight, tent, and so on). Trilobite has no unicode emoji; it is a gap.

Travel list mappings (closest glyph, not a unique icon per marketing name):

- Passenger jet / takeoff / landing → ✈️ 🛫 🛬
- Private jet / small prop → 🛩️
- Suitcase → 🧳 · backpack → 🎒 · luggage tag → 🏷️
- Compass → 🧭 · world map → 🗺️ · pin → 📍
- Boarding pass → 🎫 (ticket). Airport terminal, control tower, and gate are gaps.
- Camper van → 🚐. Class C RV, travel trailer, and teardrop camper are gaps.

Hunting list mappings:

- Whitetail / generic deer → 🦌 · moose → 🫎 · bear → 🐻 · bison → 🦬
- Duck → 🦆 · goose → 🪿 · turkey → 🦃 · retriever → 🐕
- Bow → 🏹. Elk as its own animal, mule deer vs whitetail, waterfowl species, decoys, blinds, calls, treestand, binoculars, and firearms are gaps.

## Add more emoji

`Shared/Catalog.json` is the source of truth (also copied into the keyboard target). Each item:

```json
{
  "id": "passenger-jet",
  "name": "Passenger jet",
  "emoji": "✈️",
  "keywords": ["airplane", "jet", "plane", "flight"]
}
```

For a concept with no good unicode character, omit `emoji` and set `"gap": true`. Keep `id` unique across the file.

From a text list:

```text
travel/air-travel | 🪂 | BASE jumper | parachute, jump
geography/geology | | Trilobite fossil bed | trilobite, cambrian
```

```bash
python3 scripts/import_emoji_list.py my_new_emoji.txt
python3 scripts/validate_catalog.py
```

Then rebuild in Xcode. To regenerate the whole catalog from the Python taxonomy, run `python3 scripts/generate_catalog.py` (this overwrites `Catalog.json`).

## Bundle IDs

Change these together if you need your own identifiers:

| Piece | Placeholder |
| --- | --- |
| App | `com.camptysoncapital.geomoji` |
| Keyboard | `com.camptysoncapital.geomoji.keyboard` |
| App Group (optional) | `group.com.camptysoncapital.geomoji` |

Update Signing in Xcode and `PRODUCT_BUNDLE_IDENTIFIER` on both targets. App Groups are not enabled by default so a personal team can Run without extra provisioning.

## Repo layout

```
Geomoji.xcodeproj/          Xcode project + shared Geomoji scheme
Geomoji/                    SwiftUI app
GeomojiKeyboard/            Optional keyboard extension
Shared/Catalog.json         Taxonomy and mappings
Shared/*.swift              Models, loader, favorites/recents
scripts/                    Catalog generate / import / validate
```

Requires a Mac with Xcode to compile. This environment cannot run the iOS Simulator.
