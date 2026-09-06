import SwiftUI

struct AboutView: View {
    let catalog: EmojiCatalog

    private var stats: (emoji: Int, gaps: Int) {
        let emoji = catalog.categories.reduce(0) { $0 + $1.emojiCount }
        let gaps = catalog.categories.reduce(0) { $0 + $1.gapCount }
        return (emoji, gaps)
    }

    var body: some View {
        List {
            Section("What this is") {
                Text("Geomoji is a local unicode emoji catalog for travel, geography, outdoors, hunting, fishing, wildlife, and places. Tap any glyph to copy it into Messages or any other app. It is not a sticker pack.")
            }

            Section("In this build") {
                LabeledContent("Unicode emoji", value: "\(stats.emoji)")
                LabeledContent("No-emoji-yet gaps", value: "\(stats.gaps)")
            }

            Section("Optional keyboard") {
                Text("A Geomoji keyboard can insert these same unicode characters into any text field, including Messages.")
                labeledStep("1", "On the device or simulator, open Settings > General > Keyboard > Keyboards.")
                labeledStep("2", "Tap Add New Keyboard... and choose Geomoji.")
                labeledStep("3", "While typing, hold the globe key and select Geomoji.")
                labeledStep("4", "The keyboard inserts emoji without Full Access. App and keyboard keep separate recents unless you later add the optional App Group (see the README).")
            }

            Section("Add more emoji") {
                Text("Edit Shared/Catalog.json (see the README). Add an object with a unique id, name, keywords, and an emoji string — or set gap to true when unicode has no good match.")
                    .font(.callout)
            }

            Section("Bundle IDs") {
                LabeledContent("App", value: "com.camptysoncapital.geomoji")
                LabeledContent("Keyboard", value: "com.camptysoncapital.geomoji.keyboard")
                LabeledContent("App Group (optional)", value: AppConstants.appGroupID)
            }
        }
        .navigationTitle("About")
    }

    private func labeledStep(_ number: String, _ text: String) -> some View {
        HStack(alignment: .top, spacing: 10) {
            Text(number)
                .font(.caption.weight(.bold))
                .frame(width: 22, height: 22)
                .background(Color("AccentColor").opacity(0.18), in: Circle())
            Text(text)
        }
    }
}
