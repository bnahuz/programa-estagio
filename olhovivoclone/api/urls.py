from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^paradas/$', views.ParadaList.as_view(), name='music-list'),
    url(r'^parada/(?P<pk>[0-9]+)/$', views.ParadaDetail.as_view(), name='parada-detail'),

    url(r'^linhas/$', views.LinhaList.as_view(), name='music-list'),
    url(r'^linha/(?P<pk>[0-9]+)/$', views.LinhaDetail.as_view(), name='linha-detail'),

    url(r'^veiculos/$', views.VeiculoList.as_view(), name='music-list'),
    url(r'^veiculo/(?P<pk>[0-9]+)/$', views.VeiculoDetail.as_view(), name='veiculo-detail'),
    
    url(r'^posicoes/$', views.PosicaoVeiculoList.as_view(), name='music-list'),
    url(r'^posicao/(?P<pk>[0-9]+)/$', views.PosicaoVeiculoDetail.as_view(), name='posicao-detail'),


]