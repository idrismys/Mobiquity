
import json
import urllib.request as request
import requests

# with open(https://jsonplaceholder.typicode.com/users') as json_file:
#     data = json.load(json_file)
# print(data)

# with request.urlopen('https://jsonplaceholder.typicode.com/users.json') as response:
#     if response.getcode() ==200:
#         source = response.read()
#         data = json.loads(source)
#     else:
#         print("an error occured while attempting to retrieve the data")
# print(data)

# response = requests.get("https://jsonplaceholder.typicode.com")

URL = "https://jsonplaceholder.typicode.com/users"
name = 'Delphine'
PARAMS = {'username':name}
r = requests.get(url=URL, params=PARAMS)
data = json.loads(r)
print(data)