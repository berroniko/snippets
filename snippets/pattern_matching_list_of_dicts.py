# Hettinger
# https://www.youtube.com/watch?v=ZTvwxXL37XI
# @ 25min

class SearchPattern:
    pass


def find_pattern(data, search_string):
    for elem in data:
        SearchPattern.value = search_string
        match elem:
            case {"REGISTRO": SearchPattern.value, "FACTURA": factura, "NOMBRE": nombre}:
                return {"FACTURA": factura, "NOMBRE": nombre}
