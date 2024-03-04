from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_ingrediente/<str:selected_option>", views.get_ingrediente),
    path("ricette/aggiungi/", views.aggiungi_ricetta, name="aggiungi-ricetta"),
    path('ricette/elimina/<str:codice>', views.elimina_ricetta, name='elimina_ricetta'),
    path("ingredienti", views.ingredienti, name="ingredienti"),
    path("ingredienti/<str:pk>/", views.DetailView.as_view(), name="dettaglio-ingrediente"),
]