from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('simulacao/', views.simulacao_saude, name="simulacao_saude"),
]
