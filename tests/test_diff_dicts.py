import pytest

from snippets.dictionaries import diff_dicts

a = {'u': 1, 'v': 2, 'w': 3, 'x': 4}
b = {'w': 7, 'x': 8, 'y': 5, 'z': 6}


def test_inner():
    assert diff_dicts(a=a, b=b) == {'w': -4, 'x': -4}


def test_outer():
    assert diff_dicts(a=a, b=b, mode="outer") == {'u': 1, 'v': 2, 'w': -4, 'x': -4, 'y': -5, 'z': -6}


def test_left():
    assert diff_dicts(a=a, b=b, mode="left") == {'u': 1, 'v': 2, 'w': -4, 'x': -4}


def test_right():
    assert diff_dicts(a=a, b=b, mode="right") == {'w': -4, 'x': -4, 'y': -5, 'z': -6}


def test_mode_error():
    with pytest.raises(ValueError) as e:
        diff_dicts(a=a, b=b, mode="wrong")
    assert str(e.value) == "'mode' must be one of 'inner', 'outer', 'left' or 'right'"
