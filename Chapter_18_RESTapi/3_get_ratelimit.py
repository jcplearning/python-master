import requests 

# url to get the rate limit of github api
url = "https://api.github.com/rate_limit"
headers = {}
payload = {}
# make a GET request to the url
response = requests.request("GET", url, headers=headers, data=payload)
print(response.status_code)
# print the response in json format ( rate limit of github api )
print(response.json())
