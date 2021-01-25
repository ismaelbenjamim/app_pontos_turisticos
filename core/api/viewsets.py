from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )