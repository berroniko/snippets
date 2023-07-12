from typing import Iterable, Tuple


def get_adjacents(f: float, col: Iterable[float]) -> Tuple[float, float]:
    """
    Return the tuple of adjacent numbers to number f within any iterable.

    If f is within col, the next smaller number and f are returned.
    If f is the smallest element in col, f and the next higher number are returned.

    Args:
        f: The number to search adjacents for
        col: An iterable containing numbers

    Returns:
        tuple: The adjacent numbers to f
    """
    sorted_col = sorted(col)
    if sorted_col[0] == f:
        return f, sorted_col[1]

    smaller = []
    larger_or_equal = []
    for elem in col:
        smaller.append(elem) if elem < f else larger_or_equal.append(elem)
    return max(smaller), min(larger_or_equal)