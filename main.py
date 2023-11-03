from datetime import datetime, timedelta

import requests

USERNAME = ""
TOKEN = ""

# Create user
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running graph",
    "unit": "mile",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Post value to graph

value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now().strftime('%Y%m%d')
value_parameter = {
    "date": today,
    "quantity": "3.1"
}

# response = requests.post(url=value_endpoint, json=value_parameter, headers=headers)
# print(response.text)

# Update value

update_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

update_parameter = {
    "quantity": "5"
}

response = requests.put(url=update_value_endpoint, json=update_parameter, headers=headers)

print(response.text)

