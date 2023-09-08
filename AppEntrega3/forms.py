from django import forms
from .models import Producto, Categoria, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar')