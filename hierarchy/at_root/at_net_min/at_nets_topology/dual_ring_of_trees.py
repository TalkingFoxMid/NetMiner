from data_provider import DataProvider
from hierarchy.at_root.at_net_min.at_creators.john_postel import JohnPostel
from hierarchy.at_root.at_net_min.at_creators.leonard_cleinrock import \
    LeonardCleinrock
from hierarchy.at_root.at_net_min.at_creators.norman_abramson import \
    NormanAbramson
from hierarchy.at_root.at_net_min.at_creators.paul_berer import PaulBerer
from hierarchy.at_root.at_net_min.at_creators.radia_perlman import RadiaPerlman
from hierarchy.at_root.at_net_min.at_creators.robert_kann import RobertKann
from hierarchy.at_root.at_net_min.at_creators.robert_metkalf import \
    RobertMetkalf
from hierarchy.at_root.at_net_min.at_creators.steve_kroker import SteveKroker
from hierarchy.at_root.at_net_min.at_creators.winton_serf import WintonSerf

from move_widget import MoveWidget

class DualRingOfTrees(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "nets_topology"
        )
        self.move_list = []
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "Двойное кольцо деревьев (dual-ring-of-trees)"