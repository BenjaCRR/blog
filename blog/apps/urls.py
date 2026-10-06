from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('blog/', views.lista, name='lista'),
    path('blog/<int:pk>/', views.detalle, name='detalle'),
]