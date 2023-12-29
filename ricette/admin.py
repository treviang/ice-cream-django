from django.contrib import admin

from .models import Ingrediente, Ricetta

admin.site.register(Ingrediente)
admin.site.register(Ricetta)