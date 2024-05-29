from client import CrunchyrollClient
import json

def getAllAlphabetical(client):
    target = "/content/v2/discover/browse"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    payload = {
        "n": "10000",
        "sort_by": "alphabetical",
        "ratings": "true"
    }
    response = client.session.get((client.endpoint + target), headers=headers, params=payload)
    data = json.loads(response.text)
    output = data.get("data")
    return output

def getAllNewest(client):
    target = "/content/v2/discover/browse"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    payload = {
        "n": "10000",
        "sort_by": "newest",
        "ratings": "true"
    }
    response = client.session.get((client.endpoint + target), headers=headers, params=payload)
    data = json.loads(response.text)
    output = data.get("data")
    return output

def getAllPopular(client):
    target = "/content/v2/discover/browse"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    payload = {
        "n": "10000",
        "sort_by": "popular",
        "ratings": "true"
    }
    response = client.session.get((client.endpoint + target), headers=headers, params=payload)
    data = json.loads(response.text)
    output = data.get("data")
    return output

def getCategories(client):
    target = "/content/v2/discover/categories"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    response = client.session.get((client.endpoint + target), headers=headers)
    data = json.loads(response.text)
    output = data.get("data")
    return output

def search(client, n="10000", start="0", categories=None, type=None, q="", seasonal_tag=None):
    target = "/content/v2/discover/search"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    payload = {
        "n": n,
        "q": q,
        "start": start
    }
    if categories:
        payload["categories"] = categories
    if type:
        payload["type"] = type
    if seasonal_tag:
        payload["seasonal_tag"] = seasonal_tag
    response = client.session.get((client.endpoint + target), headers=headers, params=payload)
    data = json.loads(response.text)
    output = data.get("data")
    return output

def getSimilar(client, n="5", start=None):
    target = "/content/v2/discover/{}/similar_to/{}"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    payload = {
        "n": n
    }
    if start:
        payload["start"] = start
    response = client.session.get((client.endpoint + target), headers=headers, params=payload)
    data = json.loads(response.text)
    output = data.get("data")
    return output

def getSeasonTags(client):
    target = "/content/v2/discover/seasonal_tags"
    headers = {
        "Authorization" : "Bearer {}".format(client.access_token),
        "Accept": "application/json"
    }
    response = client.session.get((client.endpoint + target), headers=headers)
    data = json.loads(response.text)
    output = data.get("data")
    return output