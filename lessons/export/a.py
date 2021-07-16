import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from named_widget import NamedWidget


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
