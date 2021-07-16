import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout
)


class LayoutWidget(QWidget):
    def __init__(self, layout_proto, layout_drawer, bg_color="white"):
        super().__init__()
        self.layout_proto = layout_proto
        self.bg_color = bg_color
        self.layout_drawer = layout_drawer
        self.init_ui()

    def init_ui(self):
        base_layout = self.layout_proto()
        self.layout_drawer(base_layout)
        self.setLayout(base_layout)
        self.setStyleSheet(f"background-color:{self.bg_color};")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_iu()

    @staticmethod
    def draw_several(layout):
        for i in range(1, 4):
            label = QLabel(str(i))
            layout.addWidget(label)

    @staticmethod
    def draw_grid(layout):
        for i in range(1, 3):
            for j in range(1, 3):
                label = QLabel(f"{i},{j}")
                layout.addWidget(label, i-1, j-1)

    @staticmethod
    def draw_form(layout):
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow("Position", QLineEdit())

    def init_iu(self):
        base_layout = QVBoxLayout()
        
        base_layout.addWidget(LayoutWidget(QVBoxLayout, self.draw_several, bg_color="#b3ffb3"))
        base_layout.addWidget(LayoutWidget(QHBoxLayout, self.draw_several, bg_color="#80dfff"))
        base_layout.addWidget(LayoutWidget(QGridLayout, self.draw_grid, bg_color="#dd99ff"))
        base_layout.addWidget(LayoutWidget(QFormLayout, self.draw_form, bg_color="#ffbb99"))

        self.setLayout(base_layout)
        self.setWindowTitle('Layouts')
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())
