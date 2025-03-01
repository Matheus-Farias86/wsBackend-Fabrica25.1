import requests

BASE_URL = "https://rickandmortyapi.com/api"

def buscar_personagem(nome):
    url = f"{BASE_URL}/character/?name={nome}"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        return dados.get("results", [])
    return None
