import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QDialog


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)

        box = QMessageBox(self)
        box.setWindowTitle("Omg")
        box.setText("Close?")
        box.addButton("Hey", QMessageBox.AcceptRole)
        box.exec_()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.label = QLabel()

        self.init_iu()

    def update_label(self):
        self.label.setText(f"Counts: {self.count}")

    def increase_button_callback(self):
        self.count += 1
        self.update_label()

    def notify_button_callback(self):
        answer = QMessageBox.question(self, "Important question", "Increase by 10?", QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.count += 10
        else:
            self.count -= 10
        self.update_label()

    def weird_button_callback(self):
        CustomDialog(self)

    def init_iu(self):
        layout = QVBoxLayout()

        self.update_label()
        layout.addWidget(self.label)

        increase_button = QPushButton(text="Increase me!")
        increase_button.clicked.connect(self.increase_button_callback)
        layout.addWidget(increase_button)

        notify_button = QPushButton(text="Notify me!")
        notify_button.clicked.connect(self.notify_button_callback)
        layout.addWidget(notify_button)

        weird_button = QPushButton(text="I'm just weird")
        weird_button.clicked.connect(self.weird_button_callback)
        layout.addWidget(weird_button)

        self.setLayout(layout)
        self.setWindowTitle('Widgets')
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())
