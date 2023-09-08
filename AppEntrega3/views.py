from django.shortcuts import render, redirect
from .forms import ProductoForm, CategoriaForm, ClienteForm
from .models import Producto, Categoria, Cliente
from .forms import BusquedaForm
from django.http import HttpResponse

def formulario_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_producto')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form})

def formulario_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'formulario_categoria.html', {'form': form})

def formulario_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_cliente')
    else:
        form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form})

def buscar(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})

def inicio(request):
    return render(request, "inicio.html")

def vista_cliente(request):
    return render(request, "vista_cliente.html")

def lista_producto(request):
    
    lista = Producto.objects.all()
    
    return render(request, "lista_producto.html", {"lista_producto": lista})

def lista_categoria(request):
    
    lista = Categoria.objects.all()
    
    return render(request, "lista_categoria.html", {"lista_categoria": lista})