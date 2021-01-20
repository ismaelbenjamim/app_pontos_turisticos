from django.db import models

class Localizacao(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=80)
    pais = models.CharField(max_length=80)
    latitude = models.IntegerField(default=0, blank=True)
    longitude = models.IntegerField(default= 0, blank=True)

    def __str__(self):
        return self.linha1
