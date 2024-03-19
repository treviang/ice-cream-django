from django import forms

from ricette.models import Miscela, Ricetta

class RicettaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RicettaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
    class Meta:
        model = Ricetta
        fields = ('codice', 'descrizione')

class MiscelaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MiscelaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
        self.fields['ingrediente'].widget.attrs['class'] = 'form-select'
        self.fields['ingrediente'].widget.attrs['style'] = 'width:auto;'
        self.fields['dosaggio'].widget.attrs['min'] = '0.01'
        self.fields['dosaggio'].widget.attrs['max'] = '100'
    class Meta:
        model = Miscela
        fields = ('ingrediente', 'dosaggio')