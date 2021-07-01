import requests

message = requests.get('http://localhost:3000')
print(message.index)
