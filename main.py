import requests
import datetime as dt
MY_USERNAME = "rahul122703"
GRAPH_ID = "pixa"
account_endpoint = "https://pixe.la/v1/users"
graph_endpoint = F"https://pixe.la/v1/users/{MY_USERNAME}/graphs"
TODAYS_DATE = dt.datetime.today().strftime('%Y%m%d')
account_parameters = {
    "token": "27december2003",
    "username": MY_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
account_post = requests.post(url=account_endpoint, json=account_parameters)

header_parameter = {
"X-USER-TOKEN": "27december2003"
}

graph_paramters = {
    "id": GRAPH_ID,
    "name": "Rahul",
    "unit": "day",
    "type": "float",
    "color": "momiji"
}
graph_post = requests.post(url=graph_endpoint, json=graph_paramters, headers=header_parameter)


pixel_parameter = {
    "date": f"{TODAYS_DATE}",
    "quantity": "4",
}
pixel_endpoint = f"https://pixe.la/v1/users/{MY_USERNAME}/graphs/{GRAPH_ID}"
pixel_post = requests.post(pixel_endpoint, json=pixel_parameter, headers=header_parameter)
print(pixel_post.text)


update_endpoint = f"{pixel_endpoint}/{TODAYS_DATE}"
update_parameter = {
    "quantity": "10",
}
update_post = requests.put(update_endpoint, json=update_parameter, headers=header_parameter)



delete_endpoint = f"{pixel_endpoint}/{TODAYS_DATE}"
delete_post = requests.delete(delete_endpoint, headers=header_parameter)
print(delete_post.text)
