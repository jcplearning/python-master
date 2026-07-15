import requests
import sys

# list of repositories of the authenticated user
url = "https://api.github.com/user/repos"

# make a GET request to the url with the authorization header
payload = {}
headers = {
 
}

response = requests.request("GET", url, headers=headers, data=payload)

# check if the response status code is 200 (OK)
if response.status_code != 200:
    print('API call failed')
    sys.exit(1)

# print the response in json format ( List of repositories of the authenticated user )
payload1 = response.json()

# print the response in text format
for item in payload1:
    print(item["id"],item["name"],item["full_name"], item["owner"]["login"])