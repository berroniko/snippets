import json

import pytest


@pytest.fixture
def ice_obs():
    with open('./tests/test_data/test_ice_observations.json') as json_file:
        data = json.load(json_file)
    return data
