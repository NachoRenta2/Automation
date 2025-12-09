import requests
import time

def test_delete_users():
    
    encabezado = {"x-api-key": "reqres-free-v1"}
    url = "https://reqres.in/api/users/2"

    
    response  = requests.delete(url,headers=encabezado)

    assert response.status_code == 204
   