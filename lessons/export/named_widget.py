from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class NamedWidget(QWidget):
    def __init__(self, name: str, callback):
        super().__init__()
        self.name = name
        self.button = QPushButton(text=f"Button {self.name}")
        self.button.clicked.connect(callback)
        self.init_iu()

    def init_iu(self):
        base_layout = QVBoxLayout()

        base_layout.addWidget(QLabel(text=f"Window {self.name}"))
        base_layout.addWidget(self.button)

        self.setLayout(base_layout)
