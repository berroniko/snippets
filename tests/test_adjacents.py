from snippets.adjacents import get_adjacents

test_list = [-5.2, -3.3, 0, 2.5, 3.0, 3.5, 4.0, 5.2, 12.0, -5.55, 8, -11]


def test_f_not_in_col():
    assert get_adjacents(f=3.2, col=test_list) == (3.0, 3.5)


def test_f_in_col():
    assert get_adjacents(f=2.5, col=test_list) == (0, 2.5)


def test_f_smallest_element():
    assert get_adjacents(f=-11, col=test_list) == (-11, -5.55)
