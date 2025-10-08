import requests
import json


def ingest_endpoint(endpoint: str):
    api_response = requests.get(endpoint)

    data = api_response.json()

    return data


test = ingest_endpoint("https://pokeapi.co/api/v2/pokemon/1")
print(json.dumps(test, indent=4))
