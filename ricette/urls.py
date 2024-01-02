from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingredienti", views.ingredienti, name="ingredienti"),
    path("ingredienti/<str:pk>/", views.DetailView.as_view(), name="dettaglio-ingrediente"),
]