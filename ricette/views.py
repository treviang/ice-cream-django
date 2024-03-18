from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from ricette.forms import MiscelaForm, RicettaForm
from .models import Ingrediente, Miscela, Ricetta
from django.views import generic
from django.contrib import messages

import logging
logger = logging.getLogger(__name__)

def index(request):
    ricette = Ricetta.objects.order_by("data_creazione")
    context = {"ricette": ricette}
    return render(request, "ricette/index.html", context)

def ingredienti(request):
    ingredienti = Ingrediente.objects.order_by("data_creazione")
    context = {"ingredienti": ingredienti}
    return render(request, "ricette/ingredienti.html", context)

def elimina_ricetta(request, codice):
    ricetta = Ricetta.objects.get(codice = codice)
    ricetta.delete()
    return index(request)

def aggiungi_ricetta(request, codice=None):
    if request.method == "POST":
        MiscelaFormSet = formset_factory(MiscelaForm, extra=1)
        if codice is None:
            ricetta_form = RicettaForm(request.POST)
        else:
            ricetta_instance = get_object_or_404(Ricetta, codice=codice)
            ricetta_form = RicettaForm(request.POST, instance=ricetta_instance)
        
        miscela_form_set = MiscelaFormSet(request.POST, request.FILES)
        if ricetta_form.is_valid():
            ricetta_form.save()
            miscele = Miscela.objects.filter(ricetta = ricetta_form['codice'].value())
            miscele.delete()
            for index, form in enumerate(miscela_form_set):
                miscela = Miscela()
                miscela.ingrediente = Ingrediente.objects.get(codice=form.data['form-'+str(index)+'-ingrediente'])
                miscela.ricetta = Ricetta.objects.get(codice=ricetta_form['codice'].value())
                miscela.dosaggio = form.data['form-'+str(index)+'-dosaggio']
                miscela.save()
            messages.success(request, ('La ricetta è stata salvata correttamente!'))
        else:
            messages.error(request, 'Errore nel salvataggio del form')
        return redirect("index")
    if codice is None:
        ricetta_form = RicettaForm()
        MiscelaFormSet = formset_factory(MiscelaForm, extra=1)
        miscela_form_set = MiscelaFormSet()
        ingredienti = Ingrediente.objects.all()
        return render(request, template_name="ricette/aggiungi-ricetta.html", context={'ricetta_form':ricetta_form, 'miscela_form':miscela_form_set, 'ingredienti': ingredienti})
    else:
        ricetta = Ricetta.objects.get(codice = codice)
        ricetta_form = RicettaForm(instance=ricetta)
        qset = Miscela.objects.filter(ricetta_id=codice)
        MiscelaFormSet = inlineformset_factory(parent_model=Ricetta, model=Miscela, form=MiscelaForm, extra=0)
        miscela_form_set = MiscelaFormSet(queryset=qset, instance=ricetta, prefix='form')
        logger.error(miscela_form_set)
        ingredienti = Ingrediente.objects.all()
        return render(request, template_name="ricette/aggiungi-ricetta.html", context={'ricetta_form':ricetta_form, 'miscela_form':miscela_form_set, 'ingredienti': ingredienti})

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
