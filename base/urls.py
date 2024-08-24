from django.urls import path
from . import views #o ponto é pra importar dessa pasta

urlpatterns = [
    path('', views.home),
    path('profissional/', views.profissional, name='profissional'),
    path('pessoal/', views.pessoal, name='pessoal'),
]