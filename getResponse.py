import requests


def getResponse(urlEnd, queryType, queryContent):
    url = "https://shazam.p.rapidapi.com/" + f'{urlEnd}'

    querystring = {
        queryType: queryContent,
        "locale": "en-US",
    }

    headers = {
        'x-rapidapi-key': "4819b84ebdmshd3385dc9375d94cp104332jsnf63093179aec",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }

    response = requests.request(
        "GET", url, headers=headers, params=querystring
    )

    return response.json()
