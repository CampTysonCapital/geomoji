import Foundation

enum AppConstants {
    /// Optional App Group for syncing favorites/recents with the keyboard.
    /// Leave unused until you add the group in both `.entitlements` files
    /// and change `sharedDefaults()` to `UserDefaults(suiteName: appGroupID)`.
    static let appGroupID = "group.com.camptysoncapital.geomoji"

    static let recentsKey = "geomoji.recents"
    static let favoritesKey = "geomoji.favorites"
    static let recentLimit = 40

    static func sharedDefaults() -> UserDefaults {
        .standard
    }
}
