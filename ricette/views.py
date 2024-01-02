from django.shortcuts import render
from .models import Ingrediente, Ricetta
from django.views import generic

def index(request):
    ricette = Ricetta.objects.order_by("data_creazione")[:5]
    context = {"ricette": ricette}
    return render(request, "ricette/index.html", context)

def ingredienti(request):
    ingredienti = Ingrediente.objects.order_by("data_creazione")[:5]
    context = {"ingredienti": ingredienti}
    return render(request, "ricette/ingredienti.html", context)

class DetailView(generic.DetailView):
    model = Ingrediente
    template_name = "ricette/dettaglio-ingrediente.html"
