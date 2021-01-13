from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class MoveWidget(QWidget):
    def __init__(self, move_list, data_provider,
                 section_name , main_window, previous_widget: "MoveWidget" = None):
        super().__init__()
        if previous_widget is None:
            self.previous_widget = self
        else:
            self.previous_widget = previous_widget
        self.data_provider = data_provider
        self.ESCAPE_KEY = 16777216
        self.section_name = section_name
        self.move_map = move_list
        self.data = data_provider.get_data(move_list, section_name)
        self.main_window = main_window
        lt = QHBoxLayout()
        lt.addWidget(QLabel(self.data))
        self.setLayout(lt)
    def get_name(self):
        return self.section_name
    def set_parent(self, parent):
        self.previous_widget = parent
    def key_press(self, key_id):
        if key_id == self.ESCAPE_KEY:
            self.main_window.setCentralWidget(
                type(self.previous_widget)(
                    self.previous_widget.move_map,
                    self.previous_widget.data_provider,
                    self.previous_widget.section_name,
                    self.previous_widget.main_window,
                    self.previous_widget.previous_widget
                )
            )
            return
        index = key_id - 49
        self.main_window.setCentralWidget(self.move_map[index])