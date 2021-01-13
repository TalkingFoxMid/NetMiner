from data_provider import DataProvider
from hierarchy.at_root.at_net_min.at_Protocols.DECnet import DECNet
from hierarchy.at_root.at_net_min.at_Protocols.AppleTalk_AFP import AppleTalk
from hierarchy.at_root.at_net_min.at_Protocols.IPX_SPX import IPXSPX
from hierarchy.at_root.at_net_min.at_Protocols.OSI import OSI
from hierarchy.at_root.at_net_min.at_Protocols.SNA import SNA
from hierarchy.at_root.at_net_min.at_Protocols.TCP_IP import TCPIP
from move_widget import MoveWidget

class Protocols(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "net_min"
        )
        self.move_list = [AppleTalk,
                          DECNet,
                          IPXSPX,
                          OSI,
                          SNA,
                          TCPIP]
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "Протоколы"