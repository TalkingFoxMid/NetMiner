from hierarchy.at_root.at_net_min.OSI_levels import OSILevels
from hierarchy.at_root.at_net_min.commutation_ways import CommutationWaysWidget
from hierarchy.at_root.at_net_min.creators import CreatorsWidget
from hierarchy.at_root.at_net_min.net_devices import NetDevices
from hierarchy.at_root.at_net_min.nets_topology import NetsTopology
from hierarchy.at_root.at_net_min.protocols import Protocols
from hierarchy.at_root.netmin import NetMinWidget
from hierarchy.at_root.netquest import NetQuestWidget
from hierarchy.root import RootWidget


class StatesProvider:
    map = {
        "root_state": RootWidget,
        "net_min": NetMinWidget,
        "net_quest": NetQuestWidget,
        "creators": CreatorsWidget,
        "commutation_ways": CommutationWaysWidget,
        "OSI_levels": OSILevels,
        "Protocols": Protocols,
        "nets_topology": NetsTopology,
        "net_devices": NetDevices
    }
    @classmethod
    def get_state(cls, state_name):
        return cls.map[state_name]