from django.urls import path
from AppEntrega3.views import *
from AppEntrega3 import views

urlpatterns = [
    path('formulario_producto/', views.formulario_producto, name='formulario_producto'),
    path('formulario_categoria/', views.formulario_categoria, name='formulario_categoria'),
    path('formulario_cliente/', views.formulario_cliente, name='formulario_cliente'),
    path('buscar/', views.buscar, name='buscar'),
    path('', inicio, name=""),
    path('lista-producto/', lista_producto, name="catalogo"),
    path('vista-cliente/', vista_cliente),
    path('inicio-categoria/', lista_categoria, name="categorias"),
]