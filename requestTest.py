import requests
import json

url = "http://127.0.0.1:7979/userAuth"

response = requests.get(url,params={"username": "larry", "password": "securepassword"})

print(response.status_code)
print(response.headers)
# print(response.content)
keys = json.loads(response.content.decode("utf-8"))
print(keys)

# response = requests.post(url,json={"username":"kevin","email":"some@email","password":"fakepassword"})
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.content.decode("utf-8"))
# keys = json.loads(response.content.decode("utf-8"))
# print(keys)