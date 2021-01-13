from data_provider import DataProvider
from hierarchy.at_root.at_net_min.at_OSI_levels.Application import Application
from hierarchy.at_root.at_net_min.at_OSI_levels.DataLink import DataLink
from hierarchy.at_root.at_net_min.at_OSI_levels.Network import Network
from hierarchy.at_root.at_net_min.at_OSI_levels.Physical import Physical
from hierarchy.at_root.at_net_min.at_OSI_levels.Presentation import \
    Presentation
from hierarchy.at_root.at_net_min.at_OSI_levels.Session import Session
from hierarchy.at_root.at_net_min.at_OSI_levels.Transport import Transport
from move_widget import MoveWidget

class OSILevels(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "net_min"
        )
        self.move_list = [Application,
                          DataLink,
                          Network,
                          Physical,
                          Presentation,
                          Session,
                          Transport]
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "Уровень модели OSI"