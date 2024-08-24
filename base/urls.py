from django.urls import path
from . import views #o ponto é pra importar dessa pasta

urlpatterns = [
    path('', views.home)
]