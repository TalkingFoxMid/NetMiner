from data_provider import DataProvider
from move_widget import MoveWidget


class HierarchyKeeper:
    def __init__(self, main_window):
        self.main_window = main_window
        self.data_provider = DataProvider()
        self.netmin_move_widget = MoveWidget(
            [],
            self.data_provider,
            "root",
            self.main_window
        )
        self.root_move_widget = MoveWidget(
            [self.netmin_move_widget],
            self.data_provider,
            "root",
            self.main_window,
            None
        )
        self.netmin_move_widget.set_parent(self.root_move_widget)

    def get_root_move_widget(self):
        return self.root_move_widget