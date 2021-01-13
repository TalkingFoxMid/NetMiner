from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class MoveWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ESCAPE_KEY = 16777216

        self.lt = QHBoxLayout()
        self.setLayout(self.lt)

    def init_label(self):
        self.lt.addWidget(QLabel(self.data))



    def key_press(self, key_id):
        if key_id == self.ESCAPE_KEY:
            self.main_window.setCentralWidget(
                self.previous_widget_class
                (
                    self.data_provider,
                    self.main_window,
                    self.states_provider
                )
            )
            return
        index = key_id - 49
        if 0 <= index < len(self.move_list):
            self.main_window.setCentralWidget(self.move_list[index](
                self.data_provider,
                self.main_window,
                self.states_provider
            ))
        else:
            return