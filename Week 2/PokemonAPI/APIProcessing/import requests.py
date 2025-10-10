import requests

endpoint = "https://swapi.dev/api/starships/"

response = requests.get(endpoint).json()

print()
