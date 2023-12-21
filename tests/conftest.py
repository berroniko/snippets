import json
from pathlib import Path

import pytest

from snippets.ListOfDict import ListOfDictContainer


@pytest.fixture
def ice_obs():
    with open('./tests/test_data/test_ice_observations.json') as json_file:
        data = json.load(json_file)
    return data


# @pytest.fixture()
# def list_of_dict(filepath=Path("./tests/test_data/test_ice_observations.json")):
#     return ListOfDictContainer(filepath=filepath)


@pytest.fixture(scope="session")
def list_of_dict(tmp_path_factory):
    content = [{"FACTURA" : "6901641743",
                "CODIGO"  : "27MP150I22",
                "PRODUCTO": "PRECIOUS FOAM 150ML",
                "NOMBRE"  : "MOUSSE NETTOYANTE INTENSE IMMORTELLE/IMORTELLE EXTRA CLEANSING FOAM",
                "REGISTRO": "1EC05650314",
                "VERSION" : "0"},
               {"FACTURA" : "6901641744",
                "CODIGO"  : "52ET001O21",
                "PRODUCTO": "OSMANTHUS EDT VIAL 1,2ML",
                "NOMBRE"  : "EAU DE TOILETTE OSMANTHUS / OSMANTHUS EAU DE TOILETTE",
                "REGISTRO": "1EC15520621",
                "VERSION" : "0"},
               {"FACTURA" : "6901641745",
                "CODIGO"  : "52ET001O22",
                "PRODUCTO": "OSMANTHUS EDT VIAL 30ML",
                "NOMBRE"  : "EAU DE TOILETTE OSMANTHUS / OSMANTHUS EAU DE TOILETTE",
                "REGISTRO": "1EC15520621",
                "VERSION" : "1"}
               ]
    filepath = tmp_path_factory.mktemp("data") / "test_instantiate_detalles.json"
    with open(filepath, 'w') as f:
        json.dump(content, f)
    lod = ListOfDictContainer(filepath=Path(filepath))
    return lod
