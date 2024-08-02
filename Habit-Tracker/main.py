import requests
TOKEN = "aksf124mksdv823rasfd3"
USER_NAME = "madnikorejo"
pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graphs_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

response = requests.post(url=graphs_endpoint, params=graph_config, headers=headers)
print(response.text)
