from django import forms

from ricette.models import Ricetta

class RicettaForm(forms.ModelForm):

    class Meta:
        model = Ricetta
        fields = ('codice', 'descrizione')