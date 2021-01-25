from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from necessidades.models import Necessidade_publica
from .serializers import NecessidadeSerializer


class NecessidadeViewSet(ModelViewSet):
    queryset = Necessidade_publica.objects.all()
    serializer_class = NecessidadeSerializer

    def list(self, request, *args, **kwargs):
        return super(NecessidadeViewSet, self).list(request, *args, **kwargs)
