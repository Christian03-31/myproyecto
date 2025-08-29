from django.shortcuts import render, redirect
from .models import christiancontacto, misaelContacto

def home(request):
    return render(request, 'home.html')

def paginachristian(request):
    if request.method == 'POST':
        christiancontacto.objects.create(
        email=request.POST['mensaje'],)
        return redirect('/christian/')
    else:
        return render(request, 'indexchristian.html')

def paginamisael(request):
    if request.method == 'POST':
        listatelefonos = request.POST.getlist('telefono[]')
        misaelContacto.objects.create(
            nombre=request.POST['nombre'], 
            apellido=request.POST['apellido'], 
            email=request.POST['correo'], 
            telefono=', '.join(listatelefonos))
        return redirect('/misael/')
    else:
        return render(request, 'indexmisael.html')




