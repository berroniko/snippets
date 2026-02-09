# Hettinger
# https://www.youtube.com/watch?v=ZTvwxXL37XI
# @ 25min

class SearchPattern:
    def __init__(self, search_dict):
        self.search_dict = search_dict
        self.value = self.search_dict.values()
        self.key = self.search_dict.keys()


def find_pattern(data, search_string):
    for elem in data:
        sp = SearchPattern(search_string)
        match elem:
            case {sp.key: sp.value, "FACTURA": factura, "NOMBRE": nombre}:
                return {"FACTURA": factura, "NOMBRE": nombre}
