from snippets.find_key_nested import gen_dict_extract


def test_find_pressure(ice_obs):
    result = gen_dict_extract("pressure", ice_obs[0])
    assert next(result) == 1016


def test_find_dict(ice_obs):
    result = gen_dict_extract("wind", ice_obs[0])
    assert next(result) == {"speed": 3.6, "deg": 230}


def test_find_id(ice_obs):
    """Three instances of id exist"""
    result = gen_dict_extract("id", ice_obs[0])
    assert list(result) == [803, 1263, 2837343]
