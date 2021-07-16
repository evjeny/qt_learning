import sys
from random import randint
from PyQt5.QtCore import QFile, QCoreApplication, Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout


def load_ui_widget(path: str):
    ui_file = QFile(path)
    ui_file.open(QFile.ReadOnly)

    return uic.loadUi(ui_file)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = load_ui_widget("assets/screen1.ui")
        self.init_iu()

    def toggled_callback(self, state):
        progress = randint(0, 100) if state else 0
        self.widget.progress_bar.setValue(progress)
        self.widget.text.setText(f"Scored: {progress}%")

    def init_iu(self):
        layout = QVBoxLayout()

        self.widget.checkbox.toggled.connect(self.toggled_callback)
        layout.addWidget(self.widget)

        self.setLayout(layout)
        self.setWindowTitle('Qt Designer')
        self.showMaximized()


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    ex = Example()
    sys.exit(app.exec_())
