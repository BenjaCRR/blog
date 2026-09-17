from django.urls import path
from . import views

urlpatterns = [
    path('ventana/', views.mi_ventana, name='ventana'),
]
