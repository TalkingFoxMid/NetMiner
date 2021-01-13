from data_provider import DataProvider
from hierarchy.root import RootWidget
from hierarchy.static_states_classes_provider import StatesProvider
from move_widget import MoveWidget


class HierarchyKeeper:
    def __init__(self, main_window):
        self.main_window = main_window
        self.data_provider = DataProvider()
        self.states_provider = StatesProvider()


    def get_root_move_widget(self):
        return RootWidget(self.data_provider, self.main_window,
                          self.states_provider)