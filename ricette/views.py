from django.http import JsonResponse
from django.shortcuts import redirect, render

from ricette.forms import MiscelaFormSet, RicettaForm
from .models import Ingrediente, Ricetta
from django.views import generic
from django.contrib import messages

def index(request):
    ricette = Ricetta.objects.order_by("data_creazione")[:5]
    context = {"ricette": ricette}
    return render(request, "ricette/index.html", context)

def ingredienti(request):
    ingredienti = Ingrediente.objects.order_by("data_creazione")[:5]
    context = {"ingredienti": ingredienti}
    return render(request, "ricette/ingredienti.html", context)

def aggiungi_ricetta(request):
	if request.method == "POST":
		ricetta_form = RicettaForm(request.POST, request.FILES)
		if ricetta_form.is_valid():
			ricetta_form.save()
			messages.success(request, ('La ricetta è stata salvata correttamente!'))
		else:
			messages.error(request, 'Errore nel salvataggio del form')
		return redirect("index")
	ricetta_form = RicettaForm()
	miscela_form = MiscelaFormSet()
	ricette = Ricetta.objects.all()
	ingredienti = Ingrediente.objects.all()
	return render(request, template_name="ricette/aggiungi-ricetta.html", context={'ricetta_form':ricetta_form, 'miscela_form':miscela_form, 'ricette':ricette, 'ingredienti': ingredienti})

def get_ingrediente(request, selected_option):
    if request.method == 'GET':
        queryset = Ingrediente.objects.filter(codice=selected_option)
        data = list(queryset.values())
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request'})

class DetailView(generic.DetailView):
    model = Ingrediente
    template_name = "ricette/dettaglio-ingrediente.html"
