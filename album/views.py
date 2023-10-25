from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Selection, Player

# Create your views here.
#Vistas genericas de django 

class SelectionListView(ListView):
    #obligatorio poner el modelo con el que va a ineractuar 
    model = Selection

class SelectionDetailView(DetailView):
    model = Selection

class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    model = Player