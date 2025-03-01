import requests
from django.conf import settings

OMDB_API_KEY = "CHAVE API OMDB email atrasado"
OMDB_BASE_URL = "http://www.omdbapi.com/"

def buscar_filme(titulo):
    params = {"apikey": OMDB_API_KEY, "s": titulo}
    response = requests.get(OMDB_BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("Search", [])
    return []
