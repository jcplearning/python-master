import requests
import json

# public repositories of github
url = "https://api.github.com/repositories"

headers = {}
payload = {}

# make a GET request to the url
response = requests.request("GET", url, headers=headers, data=payload)
print(response.status_code)
# print the response in json format ( List of public repositories )
print(response.json())

# print the response in text format
payload1 = response.text
print(payload1)

# convert the text format to json format and save it in a file

payload2 = json.loads(payload1)
with open('payload2.json','w') as f:
    json.dump(payload2,f,indent=2,sort_keys=True,ensure_ascii=False)


