import SwiftUI

@main
struct GeomojiApp: App {
    @StateObject private var store = EmojiStore()
    @StateObject private var banner = CopyBanner()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(store)
                .environmentObject(banner)
        }
    }
}

struct RootView: View {
    let catalog = CatalogLoader.load()

    var body: some View {
        TabView {
            BrowseView(catalog: catalog)
                .tabItem { Label("Browse", systemImage: "square.grid.2x2") }

            SearchView(catalog: catalog)
                .tabItem { Label("Search", systemImage: "magnifyingglass") }

            LibraryView(catalog: catalog, mode: .recents)
                .tabItem { Label("Recents", systemImage: "clock") }

            LibraryView(catalog: catalog, mode: .favorites)
                .tabItem { Label("Favorites", systemImage: "star") }
        }
        .tint(Color("AccentColor"))
        .overlay(alignment: .top) {
            BannerOverlay()
        }
    }
}

struct BannerOverlay: View {
    @EnvironmentObject private var banner: CopyBanner

    var body: some View {
        if let message = banner.message {
            Text(message)
                .font(.subheadline.weight(.semibold))
                .padding(.horizontal, 16)
                .padding(.vertical, 10)
                .background(.ultraThinMaterial, in: Capsule())
                .shadow(color: .black.opacity(0.12), radius: 8, y: 2)
                .padding(.top, 8)
                .transition(.move(edge: .top).combined(with: .opacity))
                .id(message)
        }
    }
}
