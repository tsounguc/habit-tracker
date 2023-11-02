import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":"dajkfh23hrdfahdi2uh3uhfafakjd",
    "username": "ctn",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

