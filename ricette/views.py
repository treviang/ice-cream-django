from django.shortcuts import render
from .models import Ingrediente

def index(request):
    ingredienti = Ingrediente.objects.order_by("data_creazione")[:5]
    context = {"ingredienti": ingredienti}
    return render(request, "ricette/index.html", context)
