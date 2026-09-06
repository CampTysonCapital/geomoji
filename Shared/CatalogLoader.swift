import Foundation

enum CatalogLoader {
    static func load() -> EmojiCatalog {
        let bundles = [Bundle.main]
        for bundle in bundles {
            if let url = bundle.url(forResource: "Catalog", withExtension: "json") {
                do {
                    let data = try Data(contentsOf: url)
                    return try JSONDecoder().decode(EmojiCatalog.self, from: data)
                } catch {
                    assertionFailure("Failed to decode Catalog.json: \(error)")
                }
            }
        }
        return EmojiCatalog(version: 0, title: "Geomoji", categories: [])
    }
}
