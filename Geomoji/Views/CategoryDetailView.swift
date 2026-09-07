import SwiftUI

struct CategoryDetailView: View {
    let category: EmojiCategory
    @State private var showGaps = true

    var body: some View {
        ScrollView {
            LazyVStack(alignment: .leading, spacing: 22) {
                ForEach(category.subcategories) { subcategory in
                    let items = showGaps ? subcategory.items : subcategory.items.filter { !$0.isGap }
                    if !items.isEmpty {
                        VStack(alignment: .leading, spacing: 10) {
                            Text(subcategory.name)
                                .font(.title3.weight(.semibold))
                                .padding(.horizontal, 16)

                            EmojiGrid(items: items)
                        }
                    }
                }
            }
            .padding(.vertical, 12)
        }
        .background(Color(.systemGroupedBackground))
        .navigationTitle(category.name)
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                Button {
                    showGaps.toggle()
                } label: {
                    Image(systemName: showGaps ? "circle.dashed" : "circle.dashed.inset.filled")
                }
                .accessibilityLabel(showGaps ? "Hide gaps" : "Show gaps")
            }
        }
    }
}
