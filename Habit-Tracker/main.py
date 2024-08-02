import requests
import datetime


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
today = datetime.datetime.now()

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how much did you cycle today?"),
}

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"4.5"
}

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

remove_pixel_data = {
    ""
}

# response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)
