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

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__' 

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')