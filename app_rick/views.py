import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorito

def buscarView(request):
    query = request.GET.get('nome', '') # Obtendo parametros
    species = request.GET.get('species', '')
    status = request.GET.get('status', '')

    url = "https://rickandmortyapi.com/api/character/"
    params = {}

    if query: # Verificando se a query não é vazia, caso não seja, adiciona o parametro
        params["name"] = query
    if species:
        params["species"] = species
    if status:
        params["status"] = status

    response = requests.get(url, params=params) # Fazendo a requisição
    personagens = response.json().get('results', []) if response.status_code == 200 else []

    return render(request, 'buscar.html', {
        'personagens': personagens,
        'query': query,
        'selected_species': species,
        'selected_status': status
    })

@login_required
def addfavoritoView(request, personagem_id, nome, imagem):
    if Favorito.objects.filter(usuario=request.user).count() >= 4: # Verificando se o usuário já tem 4 favoritos
        return render(request, "mensagem.html", {"mensagem": "Você só pode ter até 4 favoritos!"})

    Favorito.objects.create(usuario=request.user, personagem_id=personagem_id, nome=nome, imagem=imagem)
    return redirect("perfil") # Redirecionando para a página de perfil

@login_required
def delfavoritoView(request, personagem_id):
    Favorito.objects.filter(usuario=request.user, personagem_id=personagem_id).delete()
    return redirect("perfil")
