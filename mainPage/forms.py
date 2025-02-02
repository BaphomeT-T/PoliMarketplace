from django import forms
from publish.models import Categoria, Estado

class FiltroProductoForm(forms.Form):
    precio_min = forms.DecimalField(
        label="Desde",
        min_value=0,
        required=False
    )
    precio_max = forms.DecimalField(
        label="Hasta",
        min_value=0,
        required=False
    )
    
    nombre_producto = forms.CharField(
        label="Nombre del producto",
        required=False
    )
    
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),  # Obtiene todas las categorías
        empty_label="Selecciona una categoría",  # Esto es el texto por defecto
        required=False  # Esto permite que no sea obligatorio seleccionar una categoría
    )
    estado= forms.ModelChoiceField(
        queryset=Estado.objects.all(),  # Obtiene todas las categorías
        empty_label="Selecciona un estado",  # Esto es el texto por defecto
        required=False  # Esto permite que no sea obligatorio seleccionar una categoría
    )


