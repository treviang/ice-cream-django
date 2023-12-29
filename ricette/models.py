from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Ingrediente(models.Model):
    codice = models.CharField(primary_key=True, max_length=20)
    descrizione = models.CharField(max_length=200)
    zuccheri = models.DecimalField(max_digits=3, decimal_places=2, validators=PERCENTAGE_VALIDATOR)
    grassi = models.DecimalField(max_digits=3, decimal_places=2, validators=PERCENTAGE_VALIDATOR)
    SIng = models.DecimalField(max_digits=3, decimal_places=2, validators=PERCENTAGE_VALIDATOR)
    altri_solidi = models.DecimalField(max_digits=3, decimal_places=2, validators=PERCENTAGE_VALIDATOR)
    acqua = models.DecimalField(max_digits=3, decimal_places=2, validators=PERCENTAGE_VALIDATOR)
    PAC = models.DecimalField(max_digits=4, decimal_places=2)
    POD = models.DecimalField(max_digits=4, decimal_places=2)
    costo = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    valore_energetico = models.DecimalField(max_digits=4, decimal_places=2)
    grassi = models.DecimalField(max_digits=4, decimal_places=2)
    grassi_saturi = models.DecimalField(max_digits=4, decimal_places=2)
    carboidrati = models.DecimalField(max_digits=4, decimal_places=2)
    carboidrati_zuccheri = models.DecimalField(max_digits=4, decimal_places=2)
    proteine = models.DecimalField(max_digits=3, decimal_places=2)
    sale = models.DecimalField(max_digits=3, decimal_places=3)