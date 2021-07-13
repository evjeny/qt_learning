import sys
import random
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget


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


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget(self)
        self.names = []
        self.widgets = dict()

        self.init_iu()

    def switch_layout(self):
        name = random.choice(self.names)
        self.stack.setCurrentWidget(self.widgets[name])

    def init_iu(self):
        base_layout = QVBoxLayout()

        for i in range(1, 4):
            name = str(i)
            widget = NamedWidget(name, self.switch_layout)
            self.stack.addWidget(widget)
            self.widgets[name] = widget
            self.names.append(name)

        base_layout.addWidget(self.stack)

        self.setLayout(base_layout)
        self.setWindowTitle('Transitions')
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())
