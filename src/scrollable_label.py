from PyQt5.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget
from PyQt5 import QtCore

class ScrollableLabel(QScrollArea):
    def __init__(self, parent=None, init_data: str = ""):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setWidget(QWidget(self))
        self.label = QLabel(init_data)

        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignTop)

        self.widget().setLayout(QVBoxLayout())
        self.widget().layout().addWidget(self.label)
    def setPixmap(self, pixmap):
        self.label.setPixmap(pixmap)

    def setText(self, text):
        self.label.setText(text)
    def do_scroll(self, delta_y):
        self.verticalScrollBar().setValue(self.verticalScrollBar().value() + delta_y)
