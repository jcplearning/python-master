import requests

# public repositories of github
url = "https://api.github.com/user/repos"

# make a GET request to the url with the authorization header
payload = {}

headers = {
  'Authorization': 'Bearer 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'
}
page = 1 

while True:
    params = {'page': page, 'per_page': 10, 'sort': 'full_name', 'direction': 'asc'}

    # make a GET request to the url
    response = requests.request("GET", url, headers=headers, data=payload, params=params)
    # print the response in json format ( List of public repositories )
    respos = response.json()
    if len(respos) == 0:
        break

    print(f"Page {page}")
    for i in range(0, len(respos)):
        print(f"{respos[i]['id']} {respos[i]['name']} {respos[i]['full_name']} {respos[i]['owner']['login']}")

    page += 1

    
