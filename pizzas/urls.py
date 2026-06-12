"""Define patrones de URl para pizzas"""

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
    # Página que muestra la carta de pizzas
    path('carta/', views.carta, name='carta'),
]