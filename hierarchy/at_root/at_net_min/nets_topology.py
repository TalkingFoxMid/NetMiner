from data_provider import DataProvider
from hierarchy.at_root.at_net_min.at_nets_topology.bus import Bus
from hierarchy.at_root.at_net_min.at_nets_topology.dual_ring_of_trees import \
    DualRingOfTrees
from hierarchy.at_root.at_net_min.at_nets_topology.fully_connected_network import \
    FullyConnectedNetwork
from hierarchy.at_root.at_net_min.at_nets_topology.mesh import Mesh
from hierarchy.at_root.at_net_min.at_nets_topology.physical_star_wired_ring import \
    PhysicalStarWiredRing
from hierarchy.at_root.at_net_min.at_nets_topology.point_to_point import \
    PointToPoint
from hierarchy.at_root.at_net_min.at_nets_topology.star import Star
from hierarchy.at_root.at_net_min.at_nets_topology.tree import Tree
from move_widget import MoveWidget

class NetsTopology(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "net_min"
        )
        self.move_list = [Bus,
                          DualRingOfTrees,
                          FullyConnectedNetwork,
                          Mesh,
                          PhysicalStarWiredRing,
                          PointToPoint,
                          Star,
                          Tree]
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "Топология сетей"