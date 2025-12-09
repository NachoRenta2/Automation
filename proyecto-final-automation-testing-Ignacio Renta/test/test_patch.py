import requests

def test_patch_users():

    encabezado = {"x-api-key": "reqres-free-v1"}
    url = "https://reqres.in/api/users/2"

    data = {"name":"jose"}

    response  = requests.patch(url,headers=encabezado,json=data)

    assert response.status_code == 200
    
    
    body = response.json()

    assert body["name"] == data["name"]

    assert "updatedAt" in body
    assert isinstance(body["name"],str)

   