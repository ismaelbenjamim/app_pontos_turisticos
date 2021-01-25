from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from necessidades.api.serializers import NecessidadeSerializer
from comentarios.api.serializers import ComentarioSerializer
from localizacoes.api.serializers import LocalizacaoSerializer

from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracao = AtracaoSerializer(many=True)
    necessidade_publica = NecessidadeSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    localizacoes = LocalizacaoSerializer()
    avaliacoes = AvaliacaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'descricao_completa', 'nome', 'descricao', 'aprovado', 'atracao', 'necessidade_publica', 'comentarios', 'avaliacoes', 'localizacoes', 'foto')

    def get_descricao_completa(self, obj):
        return '%s' % (obj.nome)

