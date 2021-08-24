from django.shortcuts import render
from .models import Cliente, Producto, Orden_Compra

# Create your views here.
def lista_ventas(request):
    return render(request, 'ventas/index.html', {})
