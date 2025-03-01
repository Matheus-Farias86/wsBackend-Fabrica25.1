from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastroView, name='cadastro'),
    path('login/', views.loginView, name='login'),
    path('perfil/', views.perfilView, name='perfil'),
    path('edit_perfil/', views.editarView, name='edit_perfil'),
    path('deletar_account/', views.deletarView, name='deletar_account'),
    path('logout/', views.logoutView, name='logout'),
    path('alterar_senha/', views.alterarSenhaView, name='alterar_senha'),
]
