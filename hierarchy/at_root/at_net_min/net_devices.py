from data_provider import DataProvider
from hierarchy.at_root.at_net_min.at_net_devices.hub import Hub
from hierarchy.at_root.at_net_min.at_net_devices.modem import Modem
from hierarchy.at_root.at_net_min.at_net_devices.netcard import Netcard
from hierarchy.at_root.at_net_min.at_net_devices.router import Router
from hierarchy.at_root.at_net_min.at_net_devices.routing_switch import \
    RoutingSwitch
from hierarchy.at_root.at_net_min.at_net_devices.switch import Switch
from move_widget import MoveWidget

class NetDevices(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "net_min"
        )
        self.move_list = [Modem,
                          Netcard,
                          Hub,
                          Switch,
                          Router,
                          RoutingSwitch]
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "Сетевые устройства"