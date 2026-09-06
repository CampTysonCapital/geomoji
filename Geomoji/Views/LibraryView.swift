import SwiftUI

enum LibraryMode {
    case recents
    case favorites

    var title: String {
        switch self {
        case .recents: return "Recents"
        case .favorites: return "Favorites"
        }
    }

    var emptySystemImage: String {
        switch self {
        case .recents: return "clock"
        case .favorites: return "star"
        }
    }

    var emptyDescription: String {
        switch self {
        case .recents:
            return "Emoji you copy or insert show up here."
        case .favorites:
            return "Tap the star on any emoji to save it here."
        }
    }
}

struct LibraryView: View {
    let catalog: EmojiCatalog
    let mode: LibraryMode
    @EnvironmentObject private var store: EmojiStore

    private var items: [CatalogItem] {
        switch mode {
        case .recents:
            return store.items(ids: store.recentIDs, catalog: catalog)
        case .favorites:
            return store.items(ids: store.favoriteIDs.sorted(), catalog: catalog)
                .sorted { $0.name.localizedCaseInsensitiveCompare($1.name) == .orderedAscending }
        }
    }

    var body: some View {
        NavigationStack {
            Group {
                if items.isEmpty {
                    ContentUnavailableView(
                        mode.title,
                        systemImage: mode.emptySystemImage,
                        description: Text(mode.emptyDescription)
                    )
                } else {
                    ScrollView {
                        EmojiGrid(items: items)
                            .padding(.vertical, 12)
                    }
                    .background(Color(.systemGroupedBackground))
                }
            }
            .navigationTitle(mode.title)
        }
    }
}
