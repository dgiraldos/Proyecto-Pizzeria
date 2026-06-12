from django.shortcuts import render
from .models import Pizza
# Create your views here.

def index(request):
    """La pagina de inicio de Pizzas"""
    return render(request, 'pizzas/index.html')

def carta(request):
    """La página que muestra la carta de pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizza.html', context)