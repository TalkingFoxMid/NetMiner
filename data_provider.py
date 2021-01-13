class DataProvider:
    def get_data(self, move_list, section_name):
        return "\n".join([i.get_name() for i in move_list])