from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.menu, name = 'menu'),
    path('', views.nosotros, name = 'nosotros'),
    path('', views.contacto, name = 'contacto'),
]
