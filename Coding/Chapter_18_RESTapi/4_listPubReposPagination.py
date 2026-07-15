import requests
import json

# public repositories of github
url = "https://api.github.com/repositories"

headers = {}
payload = {}
since = 0 


for iter in range(0, 5):

    params = { 'since': since  }

    # make a GET request to the url
    response = requests.request("GET", url, headers=headers, data=payload, params=params)
    # print the response in json format ( List of public repositories )
    respos = response.json()
    since = respos[-1]['id']

    with open('restapi_pagination.txt', 'a') as f:

        for i in range(0, len(respos)):
            print(f"{respos[i]['id']} {respos[i]['name']} {respos[i]['full_name']} {respos[i]['owner']['login']}")
            f.write(f"{respos[i]['id']} {respos[i]['name']} {respos[i]['full_name']} {respos[i]['owner']['login']}\n")





