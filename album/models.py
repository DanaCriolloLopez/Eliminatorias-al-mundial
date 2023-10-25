from django.db import models #permite extraer lo de la bd 
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Selection(models.Model):
    """ seleccion de futbol  """
    #aquí estamos definiendo los atributos de la tabla 
    name = models.CharField(max_length=50)
    shield = models.ImageField(upload_to='shields/')
    team = models.ImageField(upload_to='teams/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    """ Jugadores """
    #selection, clave foranea que tiene protecciones 
    selection = models.ForeignKey('Selection', on_delete=models.PROTECT,related_name='get_players' )
    #estos don varchar en la bd 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #la imagen se va a guardar en la carpeta players
    photo = models.ImageField(upload_to='players/')
    pub_date = models.DateField(auto_now_add=True)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.IntegerField()
    #no es obligatorio
    comment = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
