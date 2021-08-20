from django.db import models
#from django.db.models.query_utils import RegisterLookupMixin
from django.utils import timezone

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_cliente = models.IntegerField()
    nombre_cliente = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=64)
    region = models.CharField(max_length=64)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    espesor = models.IntegerField()
    tipo = models.BooleanField()
    precio_neto = models.IntegerField()

class Orden_Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha_compra = models.DateField()
    tipo_compra = models.CharField(max_length=50)
    forma_pago = models.CharField(max_length=30)
    tipo_facturacion = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)

