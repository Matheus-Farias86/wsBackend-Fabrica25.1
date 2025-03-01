from django.db import models
from django.contrib.auth.models import User

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Relacionamento com a tabela User
    personagem_id = models.IntegerField()
    nome = models.CharField(max_length=100)
    imagem = models.URLField()

    def __str__(self):
        return f"{self.usuario.username} - {self.nome}"
