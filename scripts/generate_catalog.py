#!/usr/bin/env python3
"""Generate Shared/Catalog.json from the Geomoji taxonomy.

Re-run after editing the CATEGORIES list below, or edit Catalog.json directly.
Every item needs a unique id. Omit emoji (or set gap=True) for concepts with
no reasonable unicode character — the app shows a "No emoji yet" gap.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Shared" / "Catalog.json"
CATALOG_DIR = ROOT / "Shared" / "Catalog"
INDEX = CATALOG_DIR / "INDEX.md"

# Browse / keyboard chip order. Keep this list as the single source of
# top-level display order when writing Catalog.json and INDEX.md.
CATEGORY_DISPLAY_ORDER = [
    "travel",
    "geography",
    "places",
    "outdoors",
    "wildlife",
    "hunting",
    "fishing",
]


def item(item_id: str, name: str, emoji: str | None, *keywords: str, gap: bool = False) -> dict:
    data: dict = {
        "id": item_id,
        "name": name,
        "keywords": list(keywords),
    }
    if emoji:
        data["emoji"] = emoji
    if gap or not emoji:
        data["gap"] = True
        data.pop("emoji", None)
    return data


def sub(sub_id: str, name: str, items: list[dict]) -> dict:
    return {"id": sub_id, "name": name, "items": items}


def cat(cat_id: str, name: str, symbol: str, summary: str, subcategories: list[dict]) -> dict:
    return {
        "id": cat_id,
        "name": name,
        "symbol": symbol,
        "summary": summary,
        "subcategories": subcategories,
    }


CATEGORIES = [
    cat(
        "travel",
        "Travel",
        "airplane",
        "Getting there, luggage, lodging, and trip moments",
        [
            sub(
                "air-travel",
                "Air Travel",
                [
                    item("passenger-jet", "Passenger jet", "✈️", "airplane", "jet", "plane", "flight", "airliner"),
                    item("jet-takeoff", "Jet taking off", "🛫", "departure", "takeoff", "airplane"),
                    item("jet-landing", "Jet landing", "🛬", "arrival", "landing", "airplane"),
                    item("small-plane", "Private / small plane", "🛩️", "private jet", "prop", "cessna", "small airplane"),
                    item("helicopter", "Helicopter", "🚁", "chopper", "heli"),
                    item("seat", "Airplane seat", "💺", "window seat", "cabin"),
                    item("parachute", "Parachute", "🪂", "skydiving"),
                    item("airport-shuttle", "Airport shuttle", "🚌", "shuttle", "bus", "airport"),
                    item("rental-car-airport", "Rental car", "🚗", "rental", "hertz stand-in"),
                    item("ticket", "Ticket / boarding pass", "🎫", "boarding pass", "boarding", "gate pass"),
                    item("airport-terminal", "Airport terminal", None, "airport", "terminal", "concourse"),
                    item("control-tower", "Control tower", None, "tower", "atc", "airport"),
                    item("boarding-gate", "Boarding gate", None, "gate", "boarding"),
                    item("boarding-pass-detail", "Boarding pass (no unique glyph)", None, "boarding pass", "gate pass"),
                ],
            ),
            sub(
                "road-trips",
                "Road Trips",
                [
                    item("car", "Road-trip car", "🚗", "car", "auto", "sedan"),
                    item("rental-car", "Rental car", "🚗", "rental car", "hire car"),
                    item("suv", "SUV / family car", "🚙", "suv", "road trip"),
                    item("pickup", "Pickup truck", "🛻", "truck", "pickup"),
                    item("taxi", "Taxi / cab", "🚕", "cab", "taxi"),
                    item("bus", "Bus", "🚌", "coach", "shuttle"),
                    item("minibus", "Camper van / van", "🚐", "van", "camper van", "sprinter"),
                    item("motorway", "Open highway", "🛣️", "highway", "freeway", "interstate"),
                    item("fuel", "Fuel pump", "⛽", "gas", "petrol", "station"),
                    item("mountain-railway", "Scenic train", "🚞", "scenic train", "rail"),
                    item("locomotive", "Locomotive", "🚂", "steam", "train"),
                    item("passenger-train", "Passenger train", "🚆", "train", "rail"),
                    item("high-speed-train", "High-speed train", "🚄", "shinkansen", "bullet"),
                    item("bullet-train", "Bullet train", "🚅", "shinkansen"),
                    item("metro", "Metro / subway", "🚇", "subway", "underground"),
                    item("station", "Train station", "🚉", "depot", "platform"),
                    item("national-park-overlook", "Scenic overlook", "🏞️", "overlook", "viewpoint"),
                    item("motor-scooter", "Motor scooter", "🛵", "vespa"),
                    item("motorcycle", "Motorcycle", "🏍️", "motorbike"),
                    item("rv-class-c", "Class C RV", None, "rv", "motorhome", "class c"),
                    item("travel-trailer", "Travel trailer", None, "trailer", "carvan", "caravan"),
                    item("teardrop-camper", "Teardrop camper", None, "teardrop", "camper"),
                    item("roof-luggage", "Car with roof luggage", None, "roof box", "thule", "cargo box"),
                    item("rest-stop", "Highway rest stop", None, "rest area", "rest stop"),
                    item("exit-sign", "Highway exit sign", None, "exit", "off ramp"),
                    item("winding-road", "Winding mountain road", None, "switchback", "hairpin"),
                    item("scenic-route-sign", "Scenic-route sign", None, "byway", "scenic route"),
                ],
            ),
            sub(
                "cruises",
                "Cruises",
                [
                    item("passenger-ship", "Cruise ship", "🛳️", "cruise", "liner"),
                    item("ship", "Ship", "🚢", "ocean liner"),
                    item("ferry", "Ferry", "⛴️", "ferry"),
                    item("water-taxi", "Water taxi", "🚤", "speedboat", "water taxi"),
                    item("sailboat", "Sailboat", "⛵", "sail", "yacht"),
                    item("motor-boat", "Motor boat", "🛥️", "cabin cruiser"),
                    item("canoe", "Canoe", "🛶", "canoe", "paddle"),
                    item("anchor", "Anchor", "⚓", "harbor", "mooring"),
                    item("ring-buoy", "Ring buoy", "🛟", "life preserver", "safety"),
                ],
            ),
            sub(
                "international",
                "International",
                [
                    item("globe-americas", "Globe (Americas)", "🌎", "world", "earth", "americas"),
                    item("globe-europe-africa", "Globe (Europe–Africa)", "🌍", "world", "earth", "africa", "europe"),
                    item("globe-asia", "Globe (Asia–Australia)", "🌏", "world", "earth", "asia"),
                    item("world-map", "World map", "🗺️", "map", "atlas"),
                    item("passport-control", "Passport control", "🛂", "passport", "immigration"),
                    item("customs", "Customs", "🛃", "customs", "declaration"),
                    item("baggage-claim", "Baggage claim", "🛄", "carousel", "luggage claim"),
                    item("left-luggage", "Left luggage", "🛅", "locker", "storage"),
                    item("id-card", "ID card", "🪪", "identification", "license"),
                    item("currency-exchange", "Currency exchange", "💱", "forex", "money"),
                    item("night-stars", "Night skyline", "🌃", "night", "city"),
                    item("milky-way", "Milky Way", "🌌", "stars", "night"),
                    item("star", "Star", "⭐", "night", "wish"),
                ],
            ),
            sub(
                "luggage",
                "Luggage",
                [
                    item("suitcase", "Rolling suitcase", "🧳", "suitcase", "luggage", "checked bag"),
                    item("carry-on", "Carry-on", "👜", "carry-on", "cabin bag"),
                    item("backpack", "Travel backpack", "🎒", "backpack", "daypack", "rucksack"),
                    item("label", "Luggage tag", "🏷️", "tag", "label"),
                    item("closed-umbrella", "Travel umbrella", "🌂", "umbrella", "rain"),
                    item("key", "Key / keycard", "🔑", "key", "keycard"),
                    item("duffel", "Duffel bag", None, "duffel", "weekender"),
                    item("luggage-stack", "Luggage stack", None, "pile", "many bags"),
                    item("sticker-suitcase", "Sticker-covered suitcase", None, "stickers", "decals"),
                    item("neck-pillow", "Neck pillow", None, "pillow", "travel pillow"),
                    item("travel-wallet", "Travel wallet", None, "document wallet"),
                    item("passport-wallet", "Passport wallet", None, "travel wallet", "document holder"),
                    item("packing-cubes", "Packing cubes", None, "organizer", "cubes"),
                    item("toiletry-bag", "Toiletry bag", None, "dop kit", "toiletries"),
                    item("camera-bag", "Camera bag", None, "camera bag"),
                ],
            ),
            sub(
                "lodging",
                "Lodging",
                [
                    item("hotel", "Hotel", "🏨", "hotel", "inn"),
                    item("boutique-hotel", "Boutique hotel", "🏨", "boutique"),
                    item("motel", "Motel", "🏨", "roadside motel", "motor lodge"),
                    item("bellhop", "Bellhop", "🛎️", "concierge"),
                    item("room-service", "Room-service tray", "🍽️", "room service", "tray"),
                    item("hotel-keycard", "Hotel keycard", "🔑", "keycard", "key"),
                    item("bed", "Hostel / bunk room", "🛏️", "bed", "hostel", "bunk"),
                    item("couch", "Vacation rental living room", "🛋️", "vacation rental", "airbnb"),
                    item("hut", "Cabin", "🛖", "cabin", "lodge", "bungalow"),
                    item("house", "Vacation rental", "🏠", "rental", "home"),
                    item("resort", "Resort", "🏝️", "all inclusive"),
                    item("camping-lodging", "Camp lodging", "🏕️", "campground"),
                    item("tent-lodging", "Tent stay", "⛺", "tent"),
                    item("hot-springs", "Hot springs", "♨️", "onsen", "spa"),
                    item("do-not-disturb", "Do Not Disturb hanger", None, "dnd", "privacy"),
                    item("luggage-cart", "Luggage cart", None, "bell cart", "trolley"),
                ],
            ),
            sub(
                "navigation",
                "Navigation",
                [
                    item("folded-map", "Folded road map", "🗺️", "road map", "glovebox"),
                    item("map-with-route", "Map with route", "🗺️", "route", "directions"),
                    item("pin-travel", "Destination pin", "📍", "pin", "drop"),
                    item("compass-travel", "Compass", "🧭", "bearing", "navigation"),
                    item("signpost", "Directional signpost", "🪧", "wayfinding", "sign"),
                    item("guidebook", "Travel guidebook", "📖", "lonely planet stand-in", "guide"),
                    item("itinerary", "Itinerary / checklist", "📋", "checklist", "plan"),
                    item("nav-arrow", "Navigation arrow", "➡️", "turn", "navigate"),
                    item("check-mark", "Checklist done", "✅", "done", "packed"),
                    item("topo-map-travel", "Topo map", None, "contour", "usgs"),
                    item("binoculars-travel", "Binoculars", None, "binos", "optics"),
                ],
            ),
            sub(
                "travel-destinations",
                "Destinations",
                [
                    item("tropical-island", "Tropical island", "🏝️", "atoll", "caribbean"),
                    item("mountain-destination", "Mountain destination", "🏔️", "alps", "rockies"),
                    item("beach-vacation", "Beach vacation", "🏖️", "beach"),
                    item("beach-bungalow", "Beach bungalow", "🛖", "bungalow", "overwater"),
                    item("beach-chair", "Beach chair / umbrella", "⛱️", "lounge chair"),
                    item("desert-destination", "Desert destination", "🏜️", "dunes"),
                    item("snowy-destination", "Snowy destination", "❄️", "ski", "winter"),
                    item("ski-destination", "Ski destination", "🎿", "ski trip"),
                    item("city-skyline", "City skyline", "🏙️", "city"),
                    item("classical-street", "Old European street", "🏛️", "europe", "old town"),
                    item("tropical-resort", "Tropical resort", "🌴", "palm", "resort"),
                    item("mountain-lodge", "Mountain lodge", "🏔️", "lodge"),
                    item("cabin-getaway", "Cabin getaway", "🛖", "cabin"),
                    item("scenic-viewpoint", "Scenic viewpoint", "🏞️", "overlook"),
                    item("observation-deck", "Observation deck", None, "lookout", "tower view"),
                ],
            ),
            sub(
                "trip-moments",
                "Trip Moments",
                [
                    item("packed-ready", "Packed and ready", "🧳", "packed"),
                    item("leaving-home", "Leaving home", "🏠", "departure from home"),
                    item("airport-waiting", "Airport waiting", "💺", "layover", "gate"),
                    item("window-seat-view", "Window-seat view", "🪟", "window seat", "porthole"),
                    item("road-trip-snacks", "Road-trip snacks", "🥨", "snacks", "gas station food"),
                    item("popcorn-snacks", "Snack bag stand-in", "🍿", "snacks"),
                    item("selfie", "Vacation selfie", "🤳", "photo", "selfie"),
                    item("camera", "Travel photography", "📷", "camera", "photo"),
                    item("sunrise", "Sunrise destination", "🌅", "sunrise", "dawn"),
                    item("sunrise-mountains", "Sunrise over mountains", "🌄", "sunrise", "alpenglow"),
                    item("sunset", "Sunset destination", "🌇", "sunset", "dusk"),
                    item("sightseeing", "Sightseeing", "👀", "looking", "tour"),
                    item("duty-free", "Souvenir shopping", "🛍️", "souvenir", "shop"),
                    item("postcard", "Postcard", "✉️", "postcard", "letter"),
                ],
            ),
        ],
    ),
    cat(
        "geography",
        "Geography",
        "globe.americas",
        "Landforms, maps, weather, geology, and oceans",
        [
            sub(
                "landforms",
                "Landforms",
                [
                    item("mountain", "Mountain", "⛰️", "peak", "range"),
                    item("snow-mountain", "Snow-capped mountain", "🏔️", "alps", "summit"),
                    item("mount-fuji", "Mount Fuji", "🗻", "fuji", "stratovolcano"),
                    item("volcano", "Volcano", "🌋", "eruption", "lava"),
                    item("desert", "Desert", "🏜️", "dunes", "arid"),
                    item("island", "Desert island", "🏝️", "atoll", "cay"),
                    item("national-park", "National park", "🏞️", "park", "valley"),
                    item("beach-landform", "Beach", "🏖️", "coast", "shore"),
                    item("rock", "Rock / boulder", "🪨", "stone", "outcrop"),
                    item("moai", "Moai / stone monument", "🗿", "easter island", "statue"),
                    item("waterfall", "Waterfall", None, "falls", "cascade"),
                    item("glacier", "Glacier", None, "icefield", "ice"),
                    item("canyon", "Canyon", None, "gorge", "grand canyon"),
                    item("cave", "Cave", None, "cavern", "karst"),
                    item("geyser", "Geyser", None, "fumarole", "hydrothermal"),
                ],
            ),
            sub(
                "maps",
                "Maps",
                [
                    item("world-map-geo", "World map", "🗺️", "map", "atlas", "topo"),
                    item("japan-map", "Map of Japan", "🗾", "japan"),
                    item("compass", "Compass", "🧭", "bearing", "orienteering", "navigation"),
                    item("pin", "Destination pin", "📍", "pin", "marker", "drop"),
                    item("round-pushpin", "Round pushpin", "📌", "pin"),
                    item("placard", "Signpost / placard", "🪧", "sign", "wayfinding"),
                    item("straight-ruler", "Ruler / scale bar", "📏", "scale", "measure"),
                    item("triangular-ruler", "Triangle ruler", "📐", "drafting"),
                    item("binoculars", "Binoculars", None, "binos", "optics", "spotting"),
                    item("topo-map", "Topo map", None, "contour", "usgs", "quad"),
                ],
            ),
            sub(
                "weather",
                "Weather",
                [
                    item("sun", "Sun", "☀️", "clear", "sunny"),
                    item("sun-behind-small-cloud", "Mostly sunny", "🌤️", "partly cloudy"),
                    item("cloud", "Cloud", "☁️", "overcast"),
                    item("rain-cloud", "Rain", "🌧️", "shower"),
                    item("storm", "Thunderstorm", "⛈️", "storm"),
                    item("lightning", "Lightning", "⚡", "bolt", "electric"),
                    item("snowflake", "Snowflake", "❄️", "snow", "winter"),
                    item("snowman", "Snowman", "☃️", "snow"),
                    item("tornado", "Tornado / cyclone", "🌪️", "twister"),
                    item("fog", "Fog", "🌫️", "mist"),
                    item("rainbow", "Rainbow", "🌈", "prism"),
                    item("thermometer", "Thermometer", "🌡️", "temperature", "heat"),
                    item("wind-face", "Wind", "💨", "gust"),
                    item("cyclone", "Cyclone symbol", "🌀", "hurricane", "typhoon"),
                    item("umbrella-rain", "Umbrella with rain", "☔", "rain"),
                    item("comet", "Comet", "☄️", "meteor"),
                    item("water-wave-weather", "Ocean wave", "🌊", "swell", "surf"),
                    item("droplet", "Droplet", "💧", "water", "raindrop"),
                ],
            ),
            sub(
                "geology",
                "Geology",
                [
                    item("volcano-geo", "Volcano", "🌋", "igneous", "magma", "eruption"),
                    item("rock-geo", "Rock", "🪨", "lithic", "outcrop", "clast"),
                    item("gem", "Gem / crystal", "💎", "mineral", "diamond", "geode"),
                    item("bone", "Bone / fossil bone", "🦴", "fossil", "osteology"),
                    item("sauropod", "Sauropod", "🦕", "dinosaur", "jurassic"),
                    item("trex", "T-Rex", "🦖", "dinosaur", "cretaceous"),
                    item("pick", "Pick / field hammer stand-in", "⛏️", "hammer", "rock hammer", "pickaxe"),
                    item("axe", "Axe", "🪓", "hatchet", "field tool"),
                    item("test-tube", "Test tube", "🧪", "lab", "geochem"),
                    item("microscope", "Microscope", "🔬", "thin section", "petrography"),
                    item("telescope", "Telescope", "🔭", "field glass"),
                    item("magnet", "Magnet", "🧲", "paleomag"),
                    item("thermometer-geo", "Thermometer", "🌡️", "geotherm"),
                    item("collision", "Impact / eruption burst", "💥", "impact", "shock"),
                    item("hot-springs-geo", "Hot springs", "♨️", "hydrothermal", "geothermal"),
                    item("earth-americas", "Earth (Americas)", "🌎", "planet", "globe"),
                    item("earth-africa", "Earth (Africa–Europe)", "🌍", "planet"),
                    item("earth-asia", "Earth (Asia)", "🌏", "planet"),
                    item("trilobite", "Trilobite", None, "trilobite", "cambrian", "fossil"),
                    item("geode", "Geode", None, "vug", "crystal pocket"),
                    item("strata", "Rock strata / layers", None, "bedding", "stratigraphy"),
                    item("core-sample", "Core sample", None, "core", "drilling"),
                    item("amber", "Amber", None, "resin", "inclusion"),
                ],
            ),
            sub(
                "oceans",
                "Oceans",
                [
                    item("water-wave", "Ocean wave", "🌊", "sea", "swell"),
                    item("droplet-ocean", "Water", "💧", "h2o"),
                    item("spouting-whale", "Spouting whale", "🐳", "whale"),
                    item("whale", "Whale", "🐋", "cetacean"),
                    item("dolphin", "Dolphin", "🐬", "porpoise"),
                    item("shark", "Shark", "🦈", "elasmobranch"),
                    item("octopus", "Octopus", "🐙", "cephalopod"),
                    item("spiral-shell", "Seashell", "🐚", "shell", "mollusk"),
                    item("coral", "Coral", "🪸", "reef"),
                    item("anchor-ocean", "Anchor", "⚓", "mooring"),
                    item("island-ocean", "Island", "🏝️", "atoll"),
                ],
            ),
        ],
    ),
    cat(
        "outdoors",
        "Outdoors",
        "figure.hiking",
        "Hiking, camping, climbing, paddling, and cycling",
        [
            sub(
                "hiking",
                "Hiking",
                [
                    item("hiking-boot", "Hiking boot", "🥾", "boot", "trail"),
                    item("running-shoe", "Trail shoe", "👟", "sneaker"),
                    item("backpack-hike", "Daypack", "🎒", "pack"),
                    item("compass-hike", "Compass", "🧭", "navigation"),
                    item("map-hike", "Trail map", "🗺️", "map"),
                    item("evergreen", "Evergreen tree", "🌲", "pine", "fir", "spruce"),
                    item("deciduous", "Deciduous tree", "🌳", "oak", "maple"),
                    item("fallen-leaf", "Fallen leaf", "🍃", "trail"),
                    item("maple-leaf", "Maple leaf", "🍁", "autumn"),
                    item("hiker", "Walker / hiker", "🚶", "trek", "hike"),
                    item("person-walking", "Person walking", "🚶‍♂️", "hike"),
                    item("national-park-hike", "Park trail", "🏞️", "trail"),
                    item("flashlight-hike", "Flashlight", "🔦", "torch", "headlamp stand-in"),
                    item("sun-hike", "Fair weather", "☀️", "sunshine"),
                    item("mountain-hike", "Mountain trail", "⛰️", "peak"),
                    item("snow-peak-hike", "Alpine peak", "🏔️", "alpine"),
                    item("star-hike", "Night hike star", "⭐", "stargaze"),
                ],
            ),
            sub(
                "camping",
                "Camping",
                [
                    item("campsite", "Camping", "🏕️", "campground"),
                    item("tent", "Tent", "⛺", "shelter"),
                    item("fire", "Campfire", "🔥", "fire", "bonfire"),
                    item("wood", "Firewood", "🪵", "log"),
                    item("flashlight", "Flashlight", "🔦", "lantern stand-in"),
                    item("candle", "Candle / lantern glow", "🕯️", "lantern"),
                    item("cooking", "Camp cooking", "🍳", "skillet", "breakfast"),
                    item("hot-beverage", "Camp coffee", "☕", "mug", "coffee"),
                    item("hut-camp", "Camp cabin", "🛖", "lean-to"),
                    item("sleeping", "Sleeping / bedroll stand-in", "🛏️", "sleeping bag"),
                    item("mosquito", "Mosquito", "🦟", "bug"),
                    item("mushroom", "Mushroom", "🍄", "forage"),
                    item("herb", "Herb / understory", "🌿", "plant"),
                    item("four-leaf-clover", "Clover", "🍀", "meadow"),
                ],
            ),
            sub(
                "climbing",
                "Climbing",
                [
                    item("person-climbing", "Person climbing", "🧗", "climber", "boulder"),
                    item("woman-climbing", "Climber", "🧗‍♀️", "lead", "sport"),
                    item("mountain-climb", "Mountain", "⛰️", "trad", "alpine"),
                    item("snow-mountain-climb", "Alpine face", "🏔️", "ice"),
                    item("knot", "Rope / knot", "🪢", "rope", "belay"),
                    item("gloves", "Gloves", "🧤", "crack gloves"),
                    item("pick-climb", "Ice tool stand-in", "⛏️", "ice axe"),
                ],
            ),
            sub(
                "paddling",
                "Paddling",
                [
                    item("canoe-paddle", "Canoe", "🛶", "paddle", "canoe"),
                    item("rowboat", "Rowboat / raft stand-in", "🚣", "raft", "row"),
                    item("person-rowing", "Person rowing", "🚣‍♂️", "crew"),
                    item("sailboat-paddle", "Sailboat", "⛵", "sail"),
                    item("speedboat", "Speedboat", "🚤", "runabout"),
                    item("wave-paddle", "Waves", "🌊", "whitewater"),
                    item("national-park-water", "Lake / park water", "🏞️", "lake"),
                    item("swimmer", "Swimmer", "🏊", "swim"),
                    item("person-surfing", "Surfing", "🏄", "surf"),
                ],
            ),
            sub(
                "cycling",
                "Cycling",
                [
                    item("bicycle", "Bicycle", "🚲", "bike"),
                    item("cyclist", "Cyclist", "🚴", "road bike"),
                    item("mountain-biker", "Mountain biker", "🚵", "mtb", "trail"),
                    item("woman-mountain-biking", "Trail rider", "🚵‍♀️", "mtb"),
                    item("helmet", "Helmet stand-in", "⛑️", "lid"),
                    item("kick-scooter", "Kick scooter", "🛴", "scooter"),
                ],
            ),
        ],
    ),
    cat(
        "hunting",
        "Hunting",
        "hare",
        "Big game, deer, waterfowl, turkey, upland, and field gear",
        [
            sub(
                "big-game",
                "Big Game",
                [
                    item("bear", "Bear", "🐻", "black bear", "grizzly", "ursid"),
                    item("moose", "Moose", "🫎", "alces", "bull moose"),
                    item("bison", "Bison / buffalo", "🦬", "buffalo"),
                    item("boar", "Wild boar / hog", "🐗", "hog", "pig"),
                    item("deer-big", "Deer (elk stand-in)", "🦌", "elk", "wapiti", "caribou"),
                    item("wolf", "Wolf", "🐺", "canid"),
                    item("goat", "Mountain goat stand-in", "🐐", "goat", "ibex"),
                    item("ram", "Ram / sheep", "🐏", "bighorn", "sheep"),
                    item("elk", "Elk", None, "wapiti", "bugle"),
                    item("caribou", "Caribou / reindeer", None, "caribou", "reindeer"),
                    item("pronghorn", "Pronghorn", None, "antelope"),
                    item("cougar", "Cougar / mountain lion", None, "puma", "catamount"),
                ],
            ),
            sub(
                "deer",
                "Deer",
                [
                    item("whitetail", "Whitetail", "🦌", "whitetail", "buck", "doe"),
                    item("buck", "Buck", "🦌", "antlers", "whitetail buck"),
                    item("doe", "Doe", "🦌", "doe", "nanny"),
                    item("mule-deer", "Mule deer", None, "muley"),
                    item("fawn", "Fawn", None, "young deer"),
                    item("shed-antler", "Shed antler", None, "shed", "antler"),
                ],
            ),
            sub(
                "waterfowl",
                "Waterfowl",
                [
                    item("duck", "Duck / mallard stand-in", "🦆", "mallard", "drake", "hen", "dabbler"),
                    item("goose", "Goose", "🪿", "canada goose", "snow goose", "honker"),
                    item("swan", "Swan", "🦢", "tundra swan"),
                    item("feather", "Feather", "🪶", "wing"),
                    item("water-wave-fowl", "Marsh / water", "🌊", "wetland"),
                    item("dog-retriever", "Retriever", "🐕", "lab", "retriever", "dog"),
                    item("mallard-drake", "Mallard drake", None, "mallard"),
                    item("mallard-hen", "Mallard hen", None, "hen"),
                    item("pintail", "Pintail", None, "sprig"),
                    item("wood-duck", "Wood duck", None, "woodie"),
                    item("canvasback", "Canvasback", None, "can"),
                    item("teal", "Teal", None, "greenwing", "bluewing", "cinnamon teal"),
                    item("gadwall", "Gadwall", None, "gadwall"),
                    item("wigeon", "American wigeon", None, "baldpate"),
                    item("shoveler", "Northern shoveler", None, "spoonbill"),
                    item("black-duck", "American black duck", None, "black duck"),
                    item("redhead-duck", "Redhead", None, "redhead"),
                    item("scaup", "Scaup", None, "bluebill"),
                    item("ring-necked-duck", "Ring-necked duck", None, "ringneck duck"),
                    item("goldeneye", "Goldeneye", None, "whistler"),
                    item("bufflehead", "Bufflehead", None, "bufflehead"),
                    item("merganser", "Merganser", None, "sawbill"),
                    item("canada-goose", "Canada goose", None, "honker"),
                    item("snow-goose", "Snow goose", None, "speck"),
                    item("brant", "Brant", None, "brant"),
                    item("specklebelly", "Greater white-fronted goose", None, "specklebelly"),
                    item("decoy", "Decoy", None, "decoys", "spread"),
                    item("duck-decoy", "Duck decoy", None, "mallard decoy"),
                    item("goose-decoy", "Goose decoy", None, "full body", "shell"),
                    item("duck-call", "Duck / goose call", None, "call", "lanyard"),
                    item("layout-blind", "Layout / A-frame blind", None, "layout blind", "A-frame"),
                    item("duck-flag", "Waterfowl flag", None, "flagging"),
                ],
            ),
            sub(
                "turkey",
                "Turkey",
                [
                    item("wild-turkey", "Wild turkey", "🦃", "gobbler", "jake", "hen turkey"),
                    item("feather-turkey", "Turkey feather", "🪶", "beard", "fan"),
                    item("evergreen-turkey", "Woods", "🌲", "hardwoods", "roost"),
                    item("turkey-call", "Turkey call", None, "box call", "slate", "diaphragm"),
                ],
            ),
            sub(
                "upland",
                "Upland",
                [
                    item("turkey-upland", "Turkey", "🦃", "upland"),
                    item("bird", "Upland bird stand-in", "🐦", "pheasant", "quail", "grouse"),
                    item("feather-upland", "Feather", "🪶", "plume"),
                    item("dog-upland", "Bird dog", "🐕", "pointer", "setter", "spaniel"),
                    item("deciduous-upland", "Cover / hedgerow", "🌳", "crp", "cover"),
                    item("pheasant", "Pheasant", None, "ringneck", "rooster"),
                    item("quail", "Quail", None, "bobwhite"),
                    item("grouse", "Grouse", None, "ruffed", "sage"),
                ],
            ),
            sub(
                "hunting-equipment",
                "Equipment",
                [
                    item("bow-arrow", "Bow and arrow", "🏹", "bow", "archery", "compound"),
                    item("direct-hit", "Target", "🎯", "bullseye", "sight"),
                    item("flashlight-hunt", "Flashlight", "🔦", "headlamp"),
                    item("knife", "Knife", "🔪", "skinning", "blade"),
                    item("axe-hunt", "Axe / hatchet", "🪓", "camp axe"),
                    item("camping-hunt", "Camp", "🏕️", "spike camp"),
                    item("tent-hunt", "Tent", "⛺", "wall tent"),
                    item("boot-hunt", "Boot", "🥾", "pac boot"),
                    item("coat", "Coat / jacket", "🧥", "layer"),
                    item("cap", "Cap", "🧢", "hat"),
                    item("gloves-hunt", "Gloves", "🧤", "handwear"),
                    item("dog-hunt", "Hunting dog", "🐕", "hound"),
                    item("telescope-hunt", "Spotting scope stand-in", "🔭", "spotter", "glass"),
                    item("compass-hunt", "Compass", "🧭", "nav"),
                    item("map-hunt", "Map", "🗺️", "onx stand-in"),
                    item("treestand", "Treestand", None, "stand", "saddle", "hang-on"),
                    item("ground-blind", "Ground blind", None, "blind"),
                    item("game-call", "Game call", None, "grunt", "bleat", "call"),
                    item("grunt-call", "Grunt call", None, "buck grunt"),
                    item("rattling-antlers", "Rattling antlers", None, "rattle"),
                    item("binoculars-hunt", "Binoculars", None, "binos", "10x42"),
                    item("rifle", "Rifle / shotgun", None, "firearm", "slug"),
                    item("camouflage", "Camouflage", None, "camo", "pattern"),
                ],
            ),
        ],
    ),
    cat(
        "fishing",
        "Fishing",
        "fish",
        "Freshwater, saltwater, fly fishing, species, and tackle",
        [
            sub(
                "freshwater",
                "Freshwater",
                [
                    item("fishing-pole-fw", "Fishing pole", "🎣", "rod", "reel", "angler"),
                    item("fish-fw", "Fish", "🐟", "bass", "trout", "walleye", "panfish"),
                    item("canoe-fish", "Fishing canoe", "🛶", "jon boat stand-in"),
                    item("rowboat-fish", "Rowboat", "🚣", "lake boat"),
                    item("national-park-fish", "Lake / river park", "🏞️", "reservoir"),
                    item("worm", "Worm / bait", "🪱", "nightcrawler", "bait"),
                    item("droplet-fw", "Fresh water", "💧", "river"),
                ],
            ),
            sub(
                "saltwater",
                "Saltwater",
                [
                    item("tropical-fish", "Tropical / inshore fish", "🐠", "inshore", "reef"),
                    item("blowfish", "Puffer / blowfish", "🐡", "puffer"),
                    item("shark-fish", "Shark", "🦈", "offshore"),
                    item("whale-fish", "Whale", "🐋", "bluewater"),
                    item("wave-salt", "Ocean", "🌊", "surf", "jetty"),
                    item("ship-fish", "Charter boat stand-in", "🚢", "head boat"),
                    item("speedboat-fish", "Skiff / center console stand-in", "🚤", "skiff"),
                    item("anchor-fish", "Anchor", "⚓", "flats"),
                    item("island-fish", "Island / flats", "🏝️", "keys"),
                ],
            ),
            sub(
                "fly-fishing",
                "Fly Fishing",
                [
                    item("fishing-pole-fly", "Rod / fly rod stand-in", "🎣", "fly rod", "4-weight"),
                    item("feather-fly", "Feather / fly material", "🪶", "hackle", "fly"),
                    item("worm-fly", "Bait (not fly)", "🪱", "nymph stand-in"),
                    item("fish-fly", "Trout stand-in", "🐟", "trout", "steelhead"),
                    item("national-park-fly", "River", "🏞️", "tailwater", "spring creek"),
                    item("evergreen-fly", "River woods", "🌲", "canyon creek"),
                    item("fly-pattern", "Fly pattern", None, "dry fly", "streamer", "nymph"),
                    item("waders", "Waders", None, "bootfoot", "stockingfoot"),
                    item("fly-vest", "Fly vest / pack", None, "sling pack"),
                ],
            ),
            sub(
                "fish-species",
                "Species",
                [
                    item("fish", "Fish", "🐟", "bass", "trout", "salmon", "pike"),
                    item("tropical-fish-sp", "Tropical fish", "🐠", "snapper", "permit stand-in"),
                    item("blowfish-sp", "Blowfish", "🐡", "puffer"),
                    item("shark-sp", "Shark", "🦈", "mako"),
                    item("octopus-sp", "Octopus", "🐙", "cephalopod"),
                    item("squid", "Squid", "🦑", "calamari"),
                    item("shrimp", "Shrimp", "🦐", "prawn"),
                    item("lobster", "Lobster", "🦞", "bug"),
                    item("crab", "Crab", "🦀", "blue crab"),
                    item("seal", "Seal", "🦭", "pinniped"),
                ],
            ),
            sub(
                "fishing-equipment",
                "Equipment",
                [
                    item("fishing-pole", "Fishing pole", "🎣", "rod", "reel"),
                    item("bucket", "Bucket / livewell stand-in", "🪣", "bait bucket"),
                    item("canoe-eq", "Canoe", "🛶", "small craft"),
                    item("motor-boat-eq", "Boat", "🛥️", "bass boat stand-in"),
                    item("knife-fish", "Filet knife stand-in", "🔪", "filet"),
                    item("worm-eq", "Bait", "🪱", "soft plastic stand-in"),
                    item("hook-gap", "Hook / lure", None, "jig", "crankbait", "soft plastic"),
                    item("tackle-box", "Tackle box", None, "tray", "bag"),
                    item("landing-net", "Landing net", None, "net", "rubber net"),
                ],
            ),
        ],
    ),
    cat(
        "wildlife",
        "Wildlife",
        "pawprint",
        "Mammals, birds, fish, and reptiles you may actually see",
        [
            sub(
                "mammals",
                "Mammals",
                [
                    item("deer-wl", "Deer", "🦌", "ungulate"),
                    item("moose-wl", "Moose", "🫎", "moose"),
                    item("bear-wl", "Bear", "🐻", "bear"),
                    item("polar-bear", "Polar bear", "🐻‍❄️", "arctic"),
                    item("fox", "Fox", "🦊", "red fox"),
                    item("wolf-wl", "Wolf", "🐺", "coyote stand-in"),
                    item("boar-wl", "Boar", "🐗", "hog"),
                    item("bison-wl", "Bison", "🦬", "buffalo"),
                    item("rabbit", "Rabbit", "🐇", "cottontail", "hare"),
                    item("chipmunk-squirrel", "Chipmunk / squirrel", "🐿️", "ground squirrel", "chipmunk"),
                    item("beaver", "Beaver", "🦫", "rodent"),
                    item("otter", "Otter", "🦦", "river otter"),
                    item("raccoon", "Raccoon", "🦝", "procyon"),
                    item("skunk", "Skunk", "🦨", "mephitid"),
                    item("hedgehog", "Hedgehog / porcupine stand-in", "🦔", "porcupine"),
                    item("bat", "Bat", "🦇", "chiroptera"),
                    item("elk-wl", "Elk", None, "wapiti"),
                    item("coyote", "Coyote", None, "song dog"),
                ],
            ),
            sub(
                "birds",
                "Birds",
                [
                    item("duck-wl", "Duck", "🦆", "waterfowl"),
                    item("goose-wl", "Goose", "🪿", "goose"),
                    item("turkey-wl", "Turkey", "🦃", "galliform"),
                    item("eagle", "Eagle", "🦅", "raptor", "bald eagle"),
                    item("owl", "Owl", "🦉", "nocturnal"),
                    item("bird-wl", "Bird", "🐦", "passerine"),
                    item("swan-wl", "Swan", "🦢", "swan"),
                    item("flamingo", "Flamingo", "🦩", "wader"),
                    item("peacock", "Peacock", "🦚", "display"),
                    item("parrot", "Parrot", "🦜", "tropical"),
                    item("penguin", "Penguin", "🐧", "seabird"),
                    item("chicken", "Chicken / grouse stand-in", "🐔", "upland"),
                    item("feather-wl", "Feather", "🪶", "plumage"),
                    item("nest", "Nest", "🪺", "eggs"),
                    item("pheasant-wl", "Pheasant", None, "ringneck"),
                ],
            ),
            sub(
                "wildlife-fish",
                "Fish",
                [
                    item("fish-wl", "Fish", "🐟", "bony fish"),
                    item("tropical-fish-wl", "Tropical fish", "🐠", "reef"),
                    item("blowfish-wl", "Blowfish", "🐡", "tetraodontid"),
                    item("shark-wl", "Shark", "🦈", "chondrichthyan"),
                    item("whale-wl", "Whale", "🐋", "mysticete"),
                    item("dolphin-wl", "Dolphin", "🐬", "odontocete"),
                    item("seal-wl", "Seal", "🦭", "harbor seal"),
                    item("octopus-wl", "Octopus", "🐙", "octopus"),
                    item("coral-wl", "Coral", "🪸", "cnidarian"),
                    item("shell-wl", "Shell", "🐚", "gastropod"),
                ],
            ),
            sub(
                "reptiles",
                "Reptiles",
                [
                    item("snake", "Snake", "🐍", "serpent"),
                    item("turtle", "Turtle", "🐢", "tortoise"),
                    item("lizard", "Lizard", "🦎", "skink"),
                    item("crocodile", "Crocodile / alligator", "🐊", "gator"),
                    item("sauropod-wl", "Sauropod (extinct)", "🦕", "paleo"),
                    item("trex-wl", "T-Rex (extinct)", "🦖", "paleo"),
                    item("frog", "Frog / amphibian", "🐸", "amphibian"),
                    item("dragon", "Folklore dragon", "🐉", "not a field ID"),
                    item("trilobite-wl", "Trilobite (extinct)", None, "fossil"),
                ],
            ),
        ],
    ),
    cat(
        "places",
        "Places",
        "map",
        "Parks, a few states, countries, and famous destinations",
        [
            sub(
                "national-parks",
                "National Parks",
                [
                    item("park-generic", "National park", "🏞️", "nps", "park"),
                    item("park-camp", "Park campground", "🏕️", "camp"),
                    item("park-peak", "Alpine park", "🏔️", "yosemite", "tetons", "denali", "glacier"),
                    item("park-volcano", "Volcanic park", "🌋", "yellowstone", "hawaii volcanoes", "lassen"),
                    item("park-hotspring", "Hydrothermal park", "♨️", "yellowstone", "hot springs"),
                    item("park-forest", "Forest park", "🌲", "smokies", "redwoods", "olympic"),
                    item("park-desert", "Desert park", "🏜️", "arches", "canyonlands", "saguaro", "death valley"),
                    item("park-beach", "Seashore / lakeshore", "🏖️", "acadia", "olympic coast"),
                    item("park-island", "Island park", "🏝️", "virgin islands", "dry tortugas"),
                    item("park-bison", "Bison range / plains park", "🦬", "yellowstone", "badlands", "wind cave"),
                    item("park-bear", "Bear country", "🐻", "katmai", "yellowstone"),
                    item("park-gator", "Everglades stand-in", "🐊", "everglades"),
                    item("park-wave", "Coastal park", "🌊", "acadia", "olympic", "channel islands"),
                    item("grand-canyon", "Grand Canyon", None, "canyon", "arizona"),
                    item("mesa-verde", "Cliff dwelling park", None, "mesa verde"),
                ],
            ),
            sub(
                "states",
                "States",
                [
                    item("hawaii", "Hawaii", "🏝️", "hi", "aloha"),
                    item("alaska", "Alaska", "🏔️", "ak", "denali"),
                    item("arizona", "Arizona", "🏜️", "az", "sonoran"),
                    item("colorado", "Colorado", "🏔️", "co", "rockies"),
                    item("florida", "Florida", "🐊", "fl", "everglades"),
                    item("california", "California", "🌅", "ca", "pacific"),
                    item("maine", "Maine", "🦞", "me", "acadia"),
                    item("montana", "Montana", "🦬", "mt", "big sky"),
                    item("utah", "Utah", "🏜️", "ut", "canyon country"),
                    item("us-flag", "United States", "🇺🇸", "usa", "america"),
                    item("texas", "Texas", None, "tx", "lone star"),
                    item("louisiana", "Louisiana", None, "la", "bayou"),
                ],
            ),
            sub(
                "countries",
                "Countries",
                [
                    item("flag-us", "United States", "🇺🇸", "usa"),
                    item("flag-ca", "Canada", "🇨🇦", "canada"),
                    item("flag-mx", "Mexico", "🇲🇽", "mexico"),
                    item("flag-gb", "United Kingdom", "🇬🇧", "uk", "britain"),
                    item("flag-fr", "France", "🇫🇷", "france"),
                    item("flag-it", "Italy", "🇮🇹", "italy"),
                    item("flag-es", "Spain", "🇪🇸", "spain"),
                    item("flag-de", "Germany", "🇩🇪", "germany"),
                    item("flag-ch", "Switzerland", "🇨🇭", "alps"),
                    item("flag-is", "Iceland", "🇮🇸", "iceland"),
                    item("flag-no", "Norway", "🇳🇴", "fjords"),
                    item("flag-jp", "Japan", "🇯🇵", "japan"),
                    item("flag-au", "Australia", "🇦🇺", "australia"),
                    item("flag-nz", "New Zealand", "🇳🇿", "nz"),
                    item("flag-cr", "Costa Rica", "🇨🇷", "costa rica"),
                    item("flag-pe", "Peru", "🇵🇪", "peru"),
                    item("flag-ke", "Kenya", "🇰🇪", "kenya"),
                    item("flag-tz", "Tanzania", "🇹🇿", "tanzania"),
                    item("flag-eg", "Egypt", "🇪🇬", "egypt"),
                    item("flag-gr", "Greece", "🇬🇷", "greece"),
                    item("flag-za", "South Africa", "🇿🇦", "south africa"),
                    item("flag-br", "Brazil", "🇧🇷", "brazil"),
                ],
            ),
            sub(
                "destinations",
                "Famous destinations",
                [
                    item("statue-of-liberty", "Statue of Liberty", "🗽", "new york", "nyc"),
                    item("tokyo-tower", "Tokyo Tower", "🗼", "tokyo", "japan"),
                    item("classical-building", "Classical building / ruins", "🏛️", "rome", "athens", "museum"),
                    item("castle", "Castle", "🏰", "europe"),
                    item("japanese-castle", "Japanese castle", "🏯", "osaka", "himeji"),
                    item("shinto-shrine", "Shinto shrine", "⛩️", "torii", "kyoto"),
                    item("bridge", "Bridge at night", "🌉", "golden gate stand-in"),
                    item("fountain", "Fountain", "⛲", "plaza"),
                    item("cityscape", "City skyline", "🏙️", "city"),
                    item("mount-fuji-dest", "Mount Fuji", "🗻", "japan"),
                    item("volcano-dest", "Volcanic destination", "🌋", "iceland", "hawaii", "sicily"),
                    item("desert-dest", "Desert destination", "🏜️", "sahara", "moab"),
                    item("island-dest", "Tropical destination", "🏝️", "caribbean", "maldives"),
                    item("beach-dest", "Beach destination", "🏖️", "coast"),
                    item("hot-springs-dest", "Hot springs destination", "♨️", "iceland", "japan"),
                    item("moai-dest", "Easter Island", "🗿", "rapa nui"),
                    item("circus-tent", "Festival / fair", "🎪", "event"),
                    item("eiffel-tower", "Eiffel Tower", None, "paris"),
                    item("pyramids", "Pyramids of Giza", None, "egypt", "giza"),
                    item("machu-picchu", "Machu Picchu", None, "peru", "andes"),
                    item("big-ben", "Big Ben / Parliament", None, "london"),
                ],
            ),
        ],
    ),
]


def flatten_ids(categories: list[dict]) -> list[str]:
    ids: list[str] = []
    for category in categories:
        ids.append(category["id"])
        for subcategory in category["subcategories"]:
            ids.append(subcategory["id"])
            for entry in subcategory["items"]:
                ids.append(entry["id"])
    return ids


def ordered_categories() -> list[dict]:
    by_id = {category["id"]: category for category in CATEGORIES}
    missing = [cat_id for cat_id in CATEGORY_DISPLAY_ORDER if cat_id not in by_id]
    extra = [cat_id for cat_id in by_id if cat_id not in CATEGORY_DISPLAY_ORDER]
    if missing or extra:
        raise SystemExit(f"Category order mismatch: missing={missing} extra={extra}")
    return [by_id[cat_id] for cat_id in CATEGORY_DISPLAY_ORDER]


def main() -> None:
    categories = ordered_categories()
    ids = flatten_ids(categories)
    dupes = [i for i in ids if ids.count(i) > 1]
    if dupes:
        raise SystemExit(f"Duplicate ids: {sorted(set(dupes))}")

    real = 0
    gaps = 0
    for category in categories:
        for subcategory in category["subcategories"]:
            for entry in subcategory["items"]:
                if entry.get("gap"):
                    gaps += 1
                else:
                    real += 1

    payload = {
        "version": 1,
        "title": "Geomoji",
        "note": "Unicode emoji catalog. gap=true means there is no good emoji yet.",
        "categories": categories,
        "stats": {"emoji": real, "gaps": gaps, "total": real + gaps},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "version": 1,
        "title": "Geomoji",
        "note": "Per-category slices of Shared/Catalog.json. The app loads the merged file.",
        "files": [f"{category['id']}.json" for category in categories],
    }
    (CATALOG_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for category in categories:
        (CATALOG_DIR / f"{category['id']}.json").write_text(
            json.dumps(category, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    lines = [
        "# Geomoji catalog index",
        "",
        "Browse order: Travel, Geography, Places, Outdoors, Wildlife, Hunting, Fishing.",
        "",
        "Unicode emoji first. `gap` means there is no good character yet — the app shows",
        "“No emoji yet” instead of custom sticker art.",
        "",
        f"**{real} emoji · {gaps} gaps · {real + gaps} items**",
        "",
    ]
    for category in categories:
        lines.append(f"## {category['name']}")
        lines.append("")
        lines.append(f"File: `Shared/Catalog/{category['id']}.json`")
        lines.append("")
        for subcategory in category["subcategories"]:
            lines.append(f"### {category['name']} → {subcategory['name']}")
            lines.append("")
            for entry in subcategory["items"]:
                if entry.get("gap"):
                    lines.append(f"- {entry['name']} — *no emoji yet*")
                else:
                    lines.append(f"- {entry['emoji']} {entry['name']}")
            lines.append("")
    INDEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({real} emoji, {gaps} gaps, {real + gaps} items)")
    print(f"Wrote {CATALOG_DIR}/*.json and {INDEX}")


if __name__ == "__main__":
    main()
