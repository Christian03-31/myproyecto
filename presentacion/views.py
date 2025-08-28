from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def paginachristian(request):
    if request.method == 'post':
        christiancontacto.objects.create(email=request.post['mensaje'])
    else:
        return render(request, 'indexchristian.html')

def paginamisael(request):
    if request.method == 'post':
        misaelContacto.objects.create(
        nombre=request.post['nombre'], 
        apellido=request.post['apellido'], 
        email=request.post['correo'], 
        telofono=request.post['telefono[]']
    )
    else:
        return render(request, 'indexmisael.html')
    




