from rest_framework.serializers import ModelSerializer
from necessidades.models import Necessidade_publica
from necessidades.models import Necessidade_tipo

class Necessidade_tipoSerializer(ModelSerializer):
    class Meta:
        model = Necessidade_tipo
        fields = ('id', 'nome')

class NecessidadeSerializer(ModelSerializer):
    tipo = Necessidade_tipoSerializer(many=True)
    class Meta:
        model = Necessidade_publica
        fields = ('id', 'nome', 'tipo')