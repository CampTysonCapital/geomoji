import SwiftUI

struct BrowseView: View {
    let catalog: EmojiCatalog

    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns: [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)], spacing: 12) {
                    // Order comes from Shared/Catalog.json: Travel, Geography,
                    // Places, Outdoors, Wildlife, Hunting, Fishing.
                    ForEach(catalog.categories) { category in
                        NavigationLink(value: category) {
                            CategoryCard(category: category)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(16)
            }
            .background(Color(.systemGroupedBackground))
            .navigationTitle("Geomoji")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    NavigationLink {
                        AboutView(catalog: catalog)
                    } label: {
                        Image(systemName: "info.circle")
                    }
                    .accessibilityLabel("About and keyboard setup")
                }
            }
            .navigationDestination(for: EmojiCategory.self) { category in
                CategoryDetailView(category: category)
            }
        }
    }
}

struct CategoryCard: View {
    let category: EmojiCategory

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Image(systemName: category.symbol)
                .font(.title2)
                .foregroundStyle(Color("AccentColor"))
                .frame(width: 36, height: 36)
                .background(Color("AccentColor").opacity(0.14), in: RoundedRectangle(cornerRadius: 8, style: .continuous))

            Text(category.name)
                .font(.headline)
                .foregroundStyle(.primary)

            Text(category.summary)
                .font(.caption)
                .foregroundStyle(.secondary)
                .fixedSize(horizontal: false, vertical: true)

            Text("\(category.emojiCount) emoji")
                .font(.caption2.weight(.medium))
                .foregroundStyle(.tertiary)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(14)
        .background(Color(.secondarySystemGroupedBackground), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }
}
