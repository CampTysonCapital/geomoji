import SwiftUI
import UIKit

struct KeyboardView: View {
    let catalog: EmojiCatalog
    @ObservedObject var store: EmojiStore
    let needsInputModeSwitchKey: Bool
    let hasFullAccess: Bool
    let onInsert: (String) -> Void
    let onDelete: () -> Void
    let nextKeyboardAction: Selector
    let inputViewController: UIInputViewController

    @State private var categoryID: String = "recents"

    private var chips: [(id: String, name: String)] {
        [("recents", "Recents"), ("favorites", "Favorites")]
            + catalog.categories.map { ($0.id, $0.name) }
    }

    private var visibleItems: [CatalogItem] {
        switch categoryID {
        case "recents":
            let recents = store.items(ids: store.recentIDs, catalog: catalog).filter { !$0.isGap }
            if recents.isEmpty {
                return catalog.categories
                    .flatMap(\.allItems)
                    .filter { !$0.isGap }
                    .prefix(24)
                    .map { $0 }
            }
            return recents
        case "favorites":
            return store.items(ids: store.favoriteIDs.sorted(), catalog: catalog).filter { !$0.isGap }
        default:
            return catalog.categories
                .first(where: { $0.id == categoryID })?
                .allItems
                .filter { !$0.isGap } ?? []
        }
    }

    var body: some View {
        VStack(spacing: 8) {
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 6) {
                    ForEach(chips, id: \.id) { chip in
                        Button {
                            categoryID = chip.id
                        } label: {
                            Text(chip.name)
                                .font(.caption.weight(.semibold))
                                .padding(.horizontal, 10)
                                .padding(.vertical, 6)
                                .background(
                                    categoryID == chip.id
                                        ? Color(red: 0.29, green: 0.42, blue: 0.31).opacity(0.28)
                                        : Color.primary.opacity(0.06),
                                    in: Capsule()
                                )
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.horizontal, 8)
            }

            if visibleItems.isEmpty {
                Text(emptyText)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
            } else {
                ScrollView {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 44), spacing: 6)], spacing: 6) {
                        ForEach(visibleItems) { item in
                            Button {
                                onInsert(item.glyph)
                                store.recordUse(item.id)
                            } label: {
                                Text(item.glyph)
                                    .font(.system(size: 28))
                                    .frame(width: 44, height: 44)
                            }
                            .accessibilityLabel(item.name)
                        }
                    }
                    .padding(.horizontal, 8)
                }
            }

            HStack(spacing: 10) {
                if needsInputModeSwitchKey {
                    NextKeyboardButton(
                        action: nextKeyboardAction,
                        inputViewController: inputViewController
                    )
                    .frame(width: 44, height: 36)
                }

                Spacer()

                if !hasFullAccess {
                    Text("Enable Full Access to sync favorites")
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                        .lineLimit(1)
                }

                Button(action: onDelete) {
                    Image(systemName: "delete.backward")
                        .font(.title3)
                        .frame(width: 52, height: 36)
                }
                .buttonStyle(.plain)
                .accessibilityLabel("Delete")
            }
            .padding(.horizontal, 10)
            .padding(.bottom, 6)
        }
        .padding(.top, 8)
    }

    private var emptyText: String {
        switch categoryID {
        case "favorites":
            return "No favorites yet. Star them in the Geomoji app."
        case "recents":
            return "No recents yet."
        default:
            return "No emoji in this category."
        }
    }
}

struct NextKeyboardButton: UIViewRepresentable {
    let action: Selector
    let inputViewController: UIInputViewController

    func makeUIView(context: Context) -> UIButton {
        let button = UIButton(type: .system)
        button.setImage(UIImage(systemName: "globe"), for: .normal)
        button.tintColor = .label
        button.addTarget(inputViewController, action: action, for: .allTouchEvents)
        button.accessibilityLabel = "Next keyboard"
        return button
    }

    func updateUIView(_ uiView: UIButton, context: Context) {}
}
