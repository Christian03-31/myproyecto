from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def paginachristian(request):
    return render(request, 'indexchristian.html')

def paginamisael(request):
    return render(request, 'indexmisael.html')

# Create your views here.
