from django.db import models
from django.contrib.auth.models import User

class filmeFavorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Relacionamento com o usuário
    title = models.CharField(max_length=255) # Título do filme
    imdb_id = models.CharField(max_length=20, unique=True) # ID do filme para evitar duplicidade
    poster = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
