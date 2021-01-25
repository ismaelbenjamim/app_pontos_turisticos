from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from atracoes.api.viewsets import AtracaoViewSet
from core.api.viewsets import PontoTuristicoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from localizacoes.api.viewsets import LocalizacaoViewSet
from necessidades.api.viewsets import NecessidadeViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'pontoturisticos', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'localizacoes', LocalizacaoViewSet)
router.register(r'necessidades', NecessidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token/', views.obtain_auth_token),
]
