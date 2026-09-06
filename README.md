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

Mapped to the closest unicode emoji where a reasonable glyph exists. Distinctive misses stay as **gaps** (not custom sticker drawings). Full line-by-line listing: [`Shared/Catalog/INDEX.md`](Shared/Catalog/INDEX.md). Per-category JSON lives in [`Shared/Catalog/`](Shared/Catalog/). The app loads the merged [`Shared/Catalog.json`](Shared/Catalog.json).

| Category | Subcategories | File |
| --- | --- | --- |
| Travel | Air Travel, Road Trips, Cruises, International, Luggage, Lodging, Navigation, Destinations, Trip Moments | `Shared/Catalog/travel.json` |
| Geography | Landforms, Maps, Weather, Geology, Oceans | `Shared/Catalog/geography.json` |
| Outdoors | Hiking, Camping, Climbing, Paddling, Cycling | `Shared/Catalog/outdoors.json` |
| Hunting | Big Game, Deer, Waterfowl, Turkey, Upland, Equipment | `Shared/Catalog/hunting.json` |
| Fishing | Freshwater, Saltwater, Fly Fishing, Species, Equipment | `Shared/Catalog/fishing.json` |
| Wildlife | Mammals, Birds, Fish, Reptiles | `Shared/Catalog/wildlife.json` |
| Places | National Parks, States, Countries, Famous destinations | `Shared/Catalog/places.json` |

This build: **414 unicode emoji** and **101 gaps**.

Starter geology / adventure glyphs are in **Geography → Geology** and **Outdoors** (rock, gem, volcano, bone, dinosaurs, globes, pick, flashlight, tent, …). Trilobite has no unicode emoji; it is a gap.

### Travel list → unicode

- Passenger jet / takeoff / landing → ✈️ 🛫 🛬 · private / small plane → 🛩️ · helicopter → 🚁
- Ticket / boarding pass → 🎫. Airport terminal, control tower, gate, and a dedicated boarding-pass glyph are gaps.
- Airport shuttle → 🚌 · rental car → 🚗 · road-trip car → 🚗 · SUV → 🚙
- Passenger / scenic train → 🚆 🚞 · cruise / ferry / water taxi → 🛳️ ⛴️ 🚤
- Rolling suitcase → 🧳 · carry-on → 👜 · backpack → 🎒 · luggage tag → 🏷️
- Duffel, luggage stack, sticker suitcase, neck pillow, wallets, packing cubes, toiletry / camera bags are gaps
- Highway → 🛣️ · camper van → 🚐. Class C RV, trailer, teardrop, roof luggage, rest stop, exit / scenic-route signs, winding road are gaps
- Compass → 🧭 · folded / route map → 🗺️ · pin → 📍 · signpost → 🪧 · guidebook → 📖 · itinerary → 📋. Topo map and binoculars are gaps
- Island / mountain / beach / desert / snow / city → 🏝️ 🏔️ 🏖️ 🏜️ ❄️ 🏙️. Observation deck is a gap
- Hotel / motel / cabin / resort → 🏨 🛖 🏝️. Do Not Disturb hanger and luggage cart are gaps
- Packed / leaving / window seat / snacks / selfie / camera / sunrise / sunset / sightseeing / postcard → 🧳 🏠 🪟 🥨 🤳 📷 🌅 🌇 👀 ✉️

### Hunting list → unicode

- Whitetail / buck / doe → 🦌 · moose → 🫎 · bear → 🐻 · bison → 🦬 · turkey → 🦃
- Duck → 🦆 · goose → 🪿 · retriever → 🐕 · bow → 🏹
- Elk, mule deer, fawn, shed antler, pheasant, quail, grouse are gaps
- Waterfowl pack species (mallard drake/hen, pintail, wood duck, canvasback, teal, gadwall, wigeon, shoveler, black duck, redhead, scaup, ring-neck, goldeneye, bufflehead, merganser, Canada / snow / brant / white-front) are gaps — unicode has only generic 🦆 🪿
- Treestand, blinds, decoys, calls, flag, binoculars, rifle, camo are gaps

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

Then rebuild in Xcode. To regenerate the merged file, per-category slices, and `Shared/Catalog/INDEX.md` from the Python taxonomy:

```bash
python3 scripts/generate_catalog.py
```

That overwrites `Shared/Catalog.json` and `Shared/Catalog/*`.

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
Shared/Catalog.json         Merged taxonomy the app loads
Shared/Catalog/             Per-category JSON + INDEX.md
Shared/*.swift              Models, loader, favorites/recents
scripts/                    Catalog generate / import / validate
```

Requires a Mac with Xcode to compile. This environment cannot run the iOS Simulator.
