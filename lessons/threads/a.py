import sys
import time
import random
from PySide2.QtCore import QObject, QThread, Signal
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class RandomProcess(QObject):
    finished = Signal()
    state = Signal(bool)

    def run(self):
        for _ in range(10):
            time.sleep(0.5)
            self.state.emit(random.random() >= 0.5)
        self.finished.emit()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("No data")
        self.start_button = QPushButton(text="Start random process")
        self.thread: QThread = None
        self.process: QObject = None
        self.init_iu()

    def start_callback(self):
        self.start_button.setEnabled(False)

        # thread and worker should be assigned to object properties
        self.thread = QThread(self)
        self.process = RandomProcess()
        self.process.moveToThread(self.thread)

        self.thread.started.connect(self.process.run)
        self.process.finished.connect(self.thread.quit)
        self.process.finished.connect(self.process.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.process.state.connect(lambda state: self.label.setText(str(state)))
        self.thread.finished.connect(
            lambda: self.start_button.setEnabled(True)
        )

        self.thread.start()

    def init_iu(self):
        layout = QVBoxLayout()

        layout.addWidget(self.label)

        self.start_button.clicked.connect(self.start_callback)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setWindowTitle('Threads')
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())
