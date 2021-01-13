class DataProvider:
    def get_data(self, move_list, section_name):
        return "\n".join([f"{move_list.index(i) + 1}: {i.get_repr()}" for i in move_list])