from django.shortcuts import render

# Create your views here.

def index(request):
    """La pagina de inicio de Pizzas"""
    return render(request, 'pizzas/index.html')