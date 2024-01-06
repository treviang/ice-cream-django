from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ricette/aggiungi/", views.aggiungi_ricetta, name="aggiungi-ricetta"),
    path("ingredienti", views.ingredienti, name="ingredienti"),
    path("ingredienti/<str:pk>/", views.DetailView.as_view(), name="dettaglio-ingrediente"),
]