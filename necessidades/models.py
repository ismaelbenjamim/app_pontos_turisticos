from django.db import models

class Necessidade_tipo(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Necessidade_publica(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.ManyToManyField(Necessidade_tipo)

    def __str__(self):
        return self.nome
