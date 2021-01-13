from PyQt5.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget


class ScrollableLabel(QScrollArea):
    def __init__(self, parent=None, init_data: str = ""):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setWidget(QWidget(self))
        self.label = QLabel(init_data)
        self.label.setWordWrap(True)
        self.widget().setLayout(QVBoxLayout())
        self.widget().layout().addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)
