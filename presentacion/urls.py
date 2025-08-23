from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('christian/', views.paginachristian),
    path('misael/', views.paginamisael)
]