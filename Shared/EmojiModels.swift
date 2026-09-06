import Foundation

struct EmojiCatalog: Codable, Hashable {
    var version: Int
    var title: String?
    var note: String?
    var categories: [EmojiCategory]
    var stats: CatalogStats?
}

struct CatalogStats: Codable, Hashable {
    var emoji: Int?
    var gaps: Int?
    var total: Int?
}

struct EmojiCategory: Codable, Identifiable, Hashable {
    var id: String
    var name: String
    var symbol: String
    var summary: String
    var subcategories: [EmojiSubcategory]

    var allItems: [CatalogItem] {
        subcategories.flatMap(\.items)
    }

    var emojiCount: Int {
        allItems.filter { !$0.isGap }.count
    }

    var gapCount: Int {
        allItems.filter(\.isGap).count
    }
}

struct EmojiSubcategory: Codable, Identifiable, Hashable {
    var id: String
    var name: String
    var items: [CatalogItem]
}

struct CatalogItem: Codable, Identifiable, Hashable {
    var id: String
    var name: String
    var keywords: [String]
    var emoji: String?
    var gap: Bool?

    var isGap: Bool {
        if gap == true { return true }
        guard let emoji, !emoji.isEmpty else { return true }
        return false
    }

    var glyph: String {
        emoji ?? ""
    }

    var searchBlob: String {
        ([id, name, glyph] + keywords).joined(separator: " ").lowercased()
    }
}

extension EmojiCatalog {
    func item(id: String) -> CatalogItem? {
        for category in categories {
            for subcategory in category.subcategories {
                if let match = subcategory.items.first(where: { $0.id == id }) {
                    return match
                }
            }
        }
        return nil
    }

    func items(matching query: String) -> [CatalogItem] {
        let needle = query.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()
        guard !needle.isEmpty else { return [] }
        return categories
            .flatMap(\.allItems)
            .filter { $0.searchBlob.contains(needle) }
    }
}
