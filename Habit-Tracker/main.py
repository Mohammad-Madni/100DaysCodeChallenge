import requests
TOKEN = "aksf124mksdv823rasfd3"
USER_NAME = "madnikorejo"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

pixela_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graphs_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    'X-USER-TOKEN' : TOKEN
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date":"20200815",
    "quantity":"9.74",
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)
