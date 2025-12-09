import requests

def test_post_users():
    url = "https://reqres.in/api/users"
    encabezado ={"x-api-key": "reqres-free-v1"}

    payload = {"name": "Jose", "job":"Profesor"}

    response = requests.post(url,headers=encabezado,json=payload)

    #verificar que el recurso ha sido creado
    assert response.status_code == 201

    data = response.json()

    #verificar que el nombre de la respuesta sea el mismo que el enviado

    assert data ["name"] == payload [ "name"] # o poniendo "Jose"
    #data es el nombre que devuelve el servidor, payload es lo que enviamos antes
    #verificamos que guardo lo que enviamos

    #verificar que la respuesta tenga un id
    assert "id" in data