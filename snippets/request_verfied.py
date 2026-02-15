import requests

def make_request(ID, producto=1, tipo=1, session=None):
    host = "https://expedientes.medicamentos.gob.sv"
    path = "/cosmeticos/get/data/cosmeticosPresentaciones"
    url = f"{host}{path}"
    params = {'ID': ID, 'producto': producto, 'tipo': tipo}

    try:
        if session:
            response = session.get(url=url, params=params, verify=False)
        else:
            response = requests.get(url=url, params=params, verify=False)
    except requests.exceptions.ConnectionError:
        print(f"ConnectionError in Presentaciones.update(ID={ID})")
        return None

    if response.status_code != 200:
        print(f"status code: {response.status_code}")
        return None
    else:
        result = response.json()
    
    return result

if __name__ == '__main__':
    print(make_request(ID="1EC01230205", producto=1, tipo=1, session=None))
