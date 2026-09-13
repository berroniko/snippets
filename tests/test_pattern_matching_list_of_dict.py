from snippets.pattern_matching_list_of_dicts import find_pattern


def test_alt_find_key_value(list_of_dict):
    data = list_of_dict.data
    result = find_pattern(data=data, search_dict={'REGISTRO': '1EC15520621'})
    assert result == [{'CODIGO'  : '52ET001O21',
                       'FACTURA' : '6901641744',
                       'NOMBRE'  : 'EAU DE TOILETTE OSMANTHUS / OSMANTHUS EAU DE TOILETTE',
                       'PRODUCTO': 'OSMANTHUS EDT VIAL 1,2ML',
                       'REGISTRO': '1EC15520621',
                       'VERSION' : '0'},
                      {'CODIGO'  : '52ET001O22',
                       'FACTURA' : '6901641745',
                       'NOMBRE'  : 'EAU DE TOILETTE OSMANTHUS / OSMANTHUS EAU DE TOILETTE',
                       'PRODUCTO': 'OSMANTHUS EDT VIAL 30ML',
                       'REGISTRO': '1EC15520621',
                       'VERSION' : '1'}]


def test_alt_find_2_key_value(list_of_dict):
    data = list_of_dict.data
    result = find_pattern(data=data, search_dict={"REGISTRO": "1EC15520621", "VERSION": "1"})
    assert result == [{"FACTURA" : "6901641745",
                       "CODIGO"  : "52ET001O22",
                       "PRODUCTO": "OSMANTHUS EDT VIAL 30ML",
                       "NOMBRE"  : "EAU DE TOILETTE OSMANTHUS / OSMANTHUS EAU DE TOILETTE",
                       "REGISTRO": "1EC15520621",
                       "VERSION" : "1"
                       }]


def test_alt_find_kv_project(list_of_dict):
    result = list_of_dict.find(search={"REGISTRO": "1EC15520621", "VERSION": "0"},
                               display={'FACTURA': 1})
    assert result == [{'FACTURA': '6901641744'}]


def test_alt_find_kv_proj_negative(list_of_dict):
    result = list_of_dict.find(search={"REGISTRO": "1EC15520621", "VERSION": "0"},
                               display={'FACTURA': 0, "NOMBRE": 0})
    assert result == [{'CODIGO'  : '52ET001O21',
                       'PRODUCTO': 'OSMANTHUS EDT VIAL 1,2ML',
                       'REGISTRO': '1EC15520621',
                       'VERSION' : '0'}]
