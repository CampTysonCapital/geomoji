import UIKit
import SwiftUI

final class KeyboardViewController: UIInputViewController {
    private var heightConstraint: NSLayoutConstraint?
    private var host: UIHostingController<KeyboardView>?

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .secondarySystemBackground

        let root = KeyboardView(
            catalog: CatalogLoader.load(),
            store: EmojiStore(),
            needsInputModeSwitchKey: needsInputModeSwitchKey,
            hasFullAccess: hasFullAccess,
            onInsert: { [weak self] text in
                self?.textDocumentProxy.insertText(text)
            },
            onDelete: { [weak self] in
                self?.textDocumentProxy.deleteBackward()
            },
            nextKeyboardAction: #selector(handleInputModeList(from:with:)),
            inputViewController: self
        )

        let host = UIHostingController(rootView: root)
        host.view.translatesAutoresizingMaskIntoConstraints = false
        host.view.backgroundColor = .clear
        addChild(host)
        view.addSubview(host.view)
        host.didMove(toParent: self)
        self.host = host

        let height = view.heightAnchor.constraint(equalToConstant: 286)
        height.priority = .defaultHigh
        heightConstraint = height

        NSLayoutConstraint.activate([
            host.view.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            host.view.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            host.view.topAnchor.constraint(equalTo: view.topAnchor),
            host.view.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            height
        ])
    }
}
