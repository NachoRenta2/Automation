import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    encabezado ={"x-api-key": "reqres-free-v1"}
    response = requests.get(url,headers=encabezado)
    #verificar que la respuesta es correcta
    assert response.status_code == 200

    data = response.json()

    #verificar qe la clave data esta presente
    assert "data" in data

    #verificar que haya al menos un usuario en la lista
    assert len(data["data"]) > 0

    print(response.status_code)
    
    
