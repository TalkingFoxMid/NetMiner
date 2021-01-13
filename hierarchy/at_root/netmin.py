from data_provider import DataProvider
from hierarchy.at_root.at_net_min.IEEE_802 import IEEE802
from hierarchy.at_root.at_net_min.OSI_levels import OSILevels
from hierarchy.at_root.at_net_min.TCP_IP_utils import TCPIPUtils
from hierarchy.at_root.at_net_min.commutation_ways import CommutationWaysWidget
from hierarchy.at_root.at_net_min.creators import CreatorsWidget
from hierarchy.at_root.at_net_min.formats import Formats
from hierarchy.at_root.at_net_min.low_level_interfaces import \
    LowLevelInterfaces
from hierarchy.at_root.at_net_min.net_devices import NetDevices
from hierarchy.at_root.at_net_min.nets_topology import NetsTopology
from hierarchy.at_root.at_net_min.protocols import Protocols
from move_widget import MoveWidget

class NetMinWidget(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "root_state"
        )
        self.move_list = [CreatorsWidget,
                          CommutationWaysWidget,
                          OSILevels,
                          NetsTopology,
                          NetDevices,
                          LowLevelInterfaces,
                          Protocols,
                          TCPIPUtils,
                          IEEE802,
                          Formats
                          ]
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "НетМин"