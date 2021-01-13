import os

from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget


class MoveWidget(QWidget):
    def __init__(self, directory):
        super().__init__()
        self.current_directory = directory
        self.update_move_sections()
        self.ESCAPE_KEY = 16777216

        self.label = QLabel()
        self.label.setWordWrap(True)
        self.lt = QHBoxLayout()
        self.lt.addWidget(self.label)
        self.update_label_text()
        self.setLayout(self.lt)

    def update_move_sections(self):
        if os.path.isdir(self.current_directory):
            self.move_sections = os.listdir(self.current_directory)
        else:
            self.move_sections = []

    def update_label_text(self):
        if os.path.isdir(self.current_directory):
            self.label.setText("\n".join(self.move_sections))
        else:
            with open(self.current_directory, "r", encoding="utf-8") as f:
                self.label.setText(f.read())

    def init_label(self):
        self.lt.addWidget(QLabel(self.data))

    def key_press(self, key_id):
        index = key_id - 49
        if key_id == self.ESCAPE_KEY:
            if self.current_directory == "content":
                return
            self.current_directory = "/".join(
                self.current_directory.split("/")[:-1]
            )
        else:
            self.current_directory += "/" + self.move_sections[index]

        self.update_move_sections()
        self.update_label_text()
