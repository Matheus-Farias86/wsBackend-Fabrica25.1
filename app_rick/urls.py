from django.urls import path
from .views import buscarView, addfavoritoView, delfavoritoView

urlpatterns = [
    path("", buscarView, name="buscar"),
    path("favorito/adicionar/<int:personagem_id>/<str:nome>/<path:imagem>/", addfavoritoView, name="addfavoritoView"),
    path("favorito/remover/<int:personagem_id>/", delfavoritoView, name="delfavoritoView"),
]
