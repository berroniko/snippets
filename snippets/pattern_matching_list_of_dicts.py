# Hettinger
# https://www.youtube.com/watch?v=ZTvwxXL37XI
# @ 25min


# !!!!!  WIP  !!!!!


class SearchPattern:
    def __init__(self, search_dict):
        self.search_d = search_dict
        self.value = self.search_d["REGISTRO"]
        self.key = list(self.search_d.keys())[0]


def find_pattern(data, search_dict):
    results = []

    for elem in data:
        sp = SearchPattern(search_dict)
        match elem:
            case {sp.key: sp.value}:
            # case sp.search_d:
                results.append(elem)

    return results