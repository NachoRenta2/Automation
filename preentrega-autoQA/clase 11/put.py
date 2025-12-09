import requests

encabezado = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/users/2"

data = {"name":"Valentina","job":"Tutora"}

response = requests.put(url,headers=encabezado,json=data)

print(response.status_code)
print(response.json())
