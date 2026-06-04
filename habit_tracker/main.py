from idlelib.rpc import response_queue

import requests
from datetime import datetime

USERNAME = "suroj"
TOKEN = "sad1sa32d1sad65as5d64a6654sa"
GRAPH_ID= "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers = headers)
# print(response.text)

new_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2026, month=6, day=3)

# print(today.strftime("%Y%M%D"))

pixel_date = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.5"
}

# response = requests.post(url=new_pixel_endpoint, json=pixel_date,headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260603"

update_config = {
    "quantity": "10.3"
}

# response = requests.put(url=update_pixel_endpoint,json=update_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260603"

response = requests.delete(url=delete_pixel_endpoint, headers= headers)
print(response.text)


