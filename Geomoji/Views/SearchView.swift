import SwiftUI

struct SearchView: View {
    let catalog: EmojiCatalog
    @State private var query = ""

    private var results: [CatalogItem] {
        catalog.items(matching: query)
    }

    var body: some View {
        NavigationStack {
            Group {
                if query.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
                    ContentUnavailableView(
                        "Search Geomoji",
                        systemImage: "magnifyingglass",
                        description: Text("Try deer, compass, jet, trilobite, Yellowstone, or fly rod.")
                    )
                } else if results.isEmpty {
                    ContentUnavailableView.search(text: query)
                } else {
                    ScrollView {
                        EmojiGrid(items: results)
                            .padding(.vertical, 12)
                    }
                    .background(Color(.systemGroupedBackground))
                }
            }
            .navigationTitle("Search")
            .searchable(text: $query, prompt: "Name or keyword")
        }
    }
}
