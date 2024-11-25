from django.db import models


class Formacao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.nome}'


class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    site = models.URLField(default='', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} ({self.cidade})'