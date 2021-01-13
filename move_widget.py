from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class MoveWidget(QWidget):
    def __init__(self, move_list, data_provider,
                 section_name , main_window, previous_widget = None):
        super().__init__()
        if previous_widget is None:
            self.previous_widget = self
        else:
            self.previous_widget = previous_widget

        self.ESCAPE_KEY = 16777216
        self.section_name = section_name
        self.move_map = move_list
        self.data = data_provider.get_data(move_list, section_name)
        self.main_window = main_window
        lt = QHBoxLayout()
        lt.addWidget(QLabel(self.data))
        self.setLayout(lt)

    def key_press(self, key_id):
        if key_id == self.ESCAPE_KEY:
            self.main_window.setCentralWidget(self.previous_widget)