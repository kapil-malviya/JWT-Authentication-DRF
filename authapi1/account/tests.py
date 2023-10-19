'''
 A Python script that sends a POST request to 'http://127.0.0.1:8000/api/user/login/' 
 which presumably corresponds to a user login endpoint of a web API

'''


import requests
import json

URL = 'http://127.0.0.1:8000/api/user/login/'

data = {
    'email': 'harshyadav5736@gmail.com',
    'password': 'harshh'
}

headers = {'Content-Type': 'application/json'}  # Set the Content-Type header to specify JSON data

jsondata = json.dumps(data)
r = requests.post(url=URL, data=jsondata, headers=headers)

data = r.json()
print(data)
