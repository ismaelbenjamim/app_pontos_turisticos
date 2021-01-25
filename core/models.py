from django.db import models
from atracoes.models import Atracao
from necessidades.models import Necessidade_publica
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacoes.models import Localizacao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao, blank=True)
    necessidade_publica = models.ManyToManyField(Necessidade_publica, blank=True)
    comentarios = models.ManyToManyField(Comentario, blank=True)
    avaliacoes = models.ManyToManyField(Avaliacao, blank=True)
    localizacoes = models.ForeignKey(Localizacao, null=True, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.nome