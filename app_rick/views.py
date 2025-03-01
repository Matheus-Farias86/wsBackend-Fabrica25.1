from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services import buscar_personagem
from .models import Favorito

def buscarView(request):
    personagens = []
    query = request.GET.get("nome")

    if query:
        personagens = buscar_personagem(query)
    return render(request, "buscar.html", {"personagens": personagens, "query": query})

@login_required
def addfavoritoView(request, personagem_id, nome, imagem):
    if Favorito.objects.filter(usuario=request.user).count() >= 4:
        return render(request, "mensagem.html", {"mensagem": "Você só pode ter até 4 favoritos!"})

    Favorito.objects.create(usuario=request.user, personagem_id=personagem_id, nome=nome, imagem=imagem)
    return redirect("perfil")

@login_required
def delfavoritoView(request, personagem_id):
    Favorito.objects.filter(usuario=request.user, personagem_id=personagem_id).delete()
    return redirect("perfil")
