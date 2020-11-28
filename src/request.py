import os
import requests
url = 'http://127.0.0.1:8000/prediction'

# Passing an image along with post request
img = open("../test/normal.jpeg", 'rb')
files= {'sample': img }

r = requests.post(url, files=files)

# printing response
print(r.text)