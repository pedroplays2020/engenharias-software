import requests

 # Making a GET request
r = requests.get('http://85.245.94.213:7777/crypto/BTC/60')

 # check status code for response received
 # success code - 200
print(r)

 # print content of request
print(r.content)