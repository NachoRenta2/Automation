import requests

#headers = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)# le pasamos la url y una key por is nos da error 401

print(response.status_code)
data = response.json() # guardo la info que me devuelve en formato json y usarlo
print(data)