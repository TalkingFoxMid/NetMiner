from data_provider import DataProvider
from hierarchy.at_root.at_net_min.at_commutation_ways.chanells import Channels
from hierarchy.at_root.at_net_min.at_commutation_ways.half_bufferization import \
    HalfBufferization
from hierarchy.at_root.at_net_min.at_commutation_ways.packets import Packets
from hierarchy.at_root.at_net_min.at_commutation_ways.parallel_comutation import \
    ParallelCommutation
from hierarchy.at_root.at_net_min.at_commutation_ways.real_time import RealTime
from move_widget import MoveWidget

class CommutationWaysWidget(MoveWidget):
    def __init__(self, data_provider: DataProvider, main_window,
                 states_provider):
        super().__init__()
        self.states_provider = states_provider
        self.data_provider = data_provider
        self.main_window = main_window
        self.previous_widget_class = states_provider.get_state(
            "net_min"
        )
        self.move_list = [Channels,
                          HalfBufferization,
                          Packets,
                          ParallelCommutation,
                          RealTime]
        self.data = data_provider.get_data(self.move_list,
                                           self.get_repr())
        self.init_label()

    @staticmethod
    def get_repr():
        return "Способы коммутации"