import requests

server_url = "http://localhost:8000/"

rw = requests.get(server_url)
print(rw, rw.text)
