import Foundation
import SwiftUI

final class EmojiStore: ObservableObject {
    @Published private(set) var recentIDs: [String]
    @Published private(set) var favoriteIDs: Set<String>

    private let defaults: UserDefaults

    init(defaults: UserDefaults = AppConstants.sharedDefaults()) {
        self.defaults = defaults
        recentIDs = defaults.stringArray(forKey: AppConstants.recentsKey) ?? []
        let saved = defaults.stringArray(forKey: AppConstants.favoritesKey) ?? []
        favoriteIDs = Set(saved)
    }

    func isFavorite(_ id: String) -> Bool {
        favoriteIDs.contains(id)
    }

    func toggleFavorite(_ id: String) {
        if favoriteIDs.contains(id) {
            favoriteIDs.remove(id)
        } else {
            favoriteIDs.insert(id)
        }
        persist()
    }

    func recordUse(_ id: String) {
        recentIDs.removeAll { $0 == id }
        recentIDs.insert(id, at: 0)
        if recentIDs.count > AppConstants.recentLimit {
            recentIDs = Array(recentIDs.prefix(AppConstants.recentLimit))
        }
        persist()
    }

    func items(ids: [String], catalog: EmojiCatalog) -> [CatalogItem] {
        ids.compactMap { catalog.item(id: $0) }
    }

    private func persist() {
        defaults.set(recentIDs, forKey: AppConstants.recentsKey)
        defaults.set(Array(favoriteIDs).sorted(), forKey: AppConstants.favoritesKey)
    }
}

final class CopyBanner: ObservableObject {
    @Published var message: String?

    private var hideTask: Task<Void, Never>?

    func show(_ text: String) {
        message = text
        hideTask?.cancel()
        hideTask = Task { @MainActor in
            try? await Task.sleep(nanoseconds: 1_400_000_000)
            if !Task.isCancelled {
                message = nil
            }
        }
    }
}
