def diff_dicts(a: dict, b: dict, mode: str = "inner") -> dict:
    """Difference between key-value pairs of two dictionaries.

    For all modes except 'inner': Missing elements are replaced with the value '0'

    Args:
        mode: one of inner (default), outer, left, right

    Returns:
        dict a - dict b with the keys defined by mode"""

    # for Python < 3.10
    # if mode == "inner":
    #     keys = set(a.keys()).intersection(set(b.keys()))
    # elif mode == "outer":
    #     keys = set(a.keys()).union(set(b.keys()))
    # elif mode == "left":
    #     keys = set(a.keys())
    # elif mode == "right":
    #     keys = set(a.keys())
    # else:
    #     raise ValueError("mode must be one of 'inner', 'outer', 'left' or 'right'")

    match mode:
        case "inner":
            keys = set(a.keys()).intersection(set(b.keys()))
        case "outer":
            keys = set(a.keys()).union(set(b.keys()))
        case "left":
            keys = set(a.keys())
        case "right":
            keys = set(b.keys())
        case _:
            raise ValueError("'mode' must be one of 'inner', 'outer', 'left' or 'right'")

    return {k: a.get(k, 0) - b.get(k, 0) for k in keys}


def sort_dict(d: dict):
    """Sort a dictionary by its keys.

    Example:
        >>> d = {'y': 5, 'z': 6, 'w': 7, 'x': 8}
        >>> sort_dict(d)
        {'w': 7, 'x': 8, 'y': 5, 'z': 6}
    """
    return {key: d[key] for key in sorted(d)}
