from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^paradas/$', views.ParadaList.as_view(), name='music-list'),
    url(r'^linhas/$', views.LinhaList.as_view(), name='music-list'),
    url(r'^veiculos/$', views.VeiculoList.as_view(), name='music-list'),
    url(r'^posicoes/$', views.PosicaoVeiculoList.as_view(), name='music-list'),

]