import SwiftUI
import UIKit

struct EmojiGrid: View {
    let items: [CatalogItem]

    private let columns = [
        GridItem(.adaptive(minimum: 92, maximum: 120), spacing: 10)
    ]

    var body: some View {
        LazyVGrid(columns: columns, spacing: 10) {
            ForEach(items) { item in
                EmojiCell(item: item)
            }
        }
        .padding(.horizontal, 16)
    }
}

struct EmojiCell: View {
    let item: CatalogItem
    @EnvironmentObject private var store: EmojiStore
    @EnvironmentObject private var banner: CopyBanner

    var body: some View {
        Button(action: activate) {
            VStack(spacing: 6) {
                ZStack(alignment: .topTrailing) {
                    Group {
                        if item.isGap {
                            Image(systemName: "circle.dashed")
                                .font(.system(size: 28))
                                .foregroundStyle(.tertiary)
                                .frame(height: 44)
                        } else {
                            Text(item.glyph)
                                .font(.system(size: 38))
                                .frame(height: 44)
                        }
                    }
                    .frame(maxWidth: .infinity)

                    Image(systemName: store.isFavorite(item.id) ? "star.fill" : "star")
                        .font(.system(size: 10, weight: .semibold))
                        .foregroundStyle(store.isFavorite(item.id) ? Color.yellow : Color.secondary.opacity(0.7))
                        .padding(4)
                }

                Text(item.isGap ? "No emoji yet" : item.name)
                    .font(.caption2)
                    .foregroundStyle(item.isGap ? .tertiary : .secondary)
                    .multilineTextAlignment(.center)
                    .lineLimit(2)
                    .frame(maxWidth: .infinity, minHeight: 28, alignment: .top)
            }
            .padding(.top, 8)
            .padding(.bottom, 8)
            .padding(.horizontal, 4)
            .background(
                Color(.secondarySystemGroupedBackground),
                in: RoundedRectangle(cornerRadius: 14, style: .continuous)
            )
            .overlay {
                if item.isGap {
                    RoundedRectangle(cornerRadius: 14, style: .continuous)
                        .strokeBorder(style: StrokeStyle(lineWidth: 1, dash: [4]))
                        .foregroundStyle(.quaternary)
                }
            }
        }
        .buttonStyle(.plain)
        .accessibilityLabel(accessibilityText)
        .contextMenu {
            if !item.isGap {
                Button("Copy \(item.glyph)", systemImage: "doc.on.doc") {
                    activate()
                }
            }
            Button(store.isFavorite(item.id) ? "Remove Favorite" : "Add Favorite", systemImage: "star") {
                store.toggleFavorite(item.id)
            }
        }
    }

    private var accessibilityText: String {
        if item.isGap {
            return "\(item.name). No emoji yet"
        }
        return "\(item.name). \(item.glyph)"
    }

    private func activate() {
        if item.isGap {
            banner.show("No emoji yet — \(item.name)")
            UINotificationFeedbackGenerator().notificationOccurred(.warning)
            return
        }
        UIPasteboard.general.string = item.glyph
        store.recordUse(item.id)
        banner.show("Copied \(item.glyph)")
        UINotificationFeedbackGenerator().notificationOccurred(.success)
    }
}
