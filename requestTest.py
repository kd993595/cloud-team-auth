import requests
import json

url = "http://127.0.0.1:7979/userAuth"



print("creating a user: ")
response = requests.post(url,json={"username":"ferguson","email":"fake@email.com","password":"securepassword"})
print(response.status_code)
print(response.headers)
print(response.content)
# print(response.content.decode("utf-8"))
# keys = json.loads(response.content.decode("utf-8"))
# print(keys)


print("getting a user token: ")
response = requests.get(url,params={"username": "ferguson", "password": "securepassword"})
print(response.status_code)
print(response.headers)
print(response.content)
# keys = json.loads(response.content.decode("utf-8"))
# print(keys)

