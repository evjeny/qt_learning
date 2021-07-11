import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_iu()

    def init_iu(self):
        layout = QVBoxLayout()

        label = QLabel("I am label")
        layout.addWidget(label)

        button = QPushButton(text="I am button")
        layout.addWidget(button)

        image = QLabel()
        pixmap = QPixmap()
        with open("assets/python_logo.png", "rb") as f:
            content = f.read()
        pixmap.loadFromData(content)
        image.setPixmap(pixmap)
        layout.addWidget(image)

        self.setLayout(layout)
        self.setWindowTitle('Widgets')
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())
