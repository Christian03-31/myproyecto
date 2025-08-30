from django.db import models

class christiancontacto(models.Model):
    email = models.EmailField()
    habilidades = models.TextField(default='No especificado')
    
    def __str__(self):
        return ('contacto '+self.email)

# Create your models here.


#misael
class misaelContacto(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email = models.EmailField()
    telefono=models.TextField()
    
    def __str__(self):
        return ('contacto ' + self.nombre +' '+ self.apellido + ' ' + self.email)
    
