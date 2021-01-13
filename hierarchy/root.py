from data_provider import DataProvider
from hierarchy.at_root.netmin import NetMinWidget
from hierarchy.at_root.netquest import NetQuestWidget
from move_widget import MoveWidget


class RootWidget(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = RootWidget
        self.move_list = [NetMinWidget, NetQuestWidget]
        self.data = data_provider.get_data(self.move_list,
                                           type(self).get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "root_state"