import requests
    
encabezado = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/users/2"

    

response  = requests.delete(url,headers=encabezado)

print(response.status_code)

print(response.text)
#eliminamos el contenido de 2, todo el recurso 2 dentro de la db users
#devuelve 204


