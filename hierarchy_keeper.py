from data_provider import DataProvider
from move_widget import MoveWidget


class HierarchyKeeper:
    def __init__(self, main_window):
        self.main_window = main_window
        self.data_provider = DataProvider()
        self.root_move_widget = MoveWidget(
            [],
            self.data_provider,
            "section_name",
            self.main_window,
            None
        )

    def get_root_move_widget(self):
        return self.root_move_widget