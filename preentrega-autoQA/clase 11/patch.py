import requests
import time

def test_put_users():
    
    encabezado = {"x-api-key": "reqres-free-v1"}
    url = "https://reqres.in/api/users/2"

    data = {"name":"jose"}

    response  = requests.patch(url,headers=encabezado,json=data)

    print(response.status_code)
    print(response.json())

    
