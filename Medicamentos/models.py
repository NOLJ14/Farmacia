from django.db import models
from django.utils.safestring import mark_safe

class Pildora(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nit=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellidoPaterno=models.CharField(max_length=30)
    apellidoMaterno=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)

class Empleado(models.Model):
    idEmpleado=models.IntegerField(primary_key=True)
    idUsuario=models.IntegerField()
    ci=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellidoPaterno=models.CharField(max_length=30)
    apellidoMaterno=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)
    telefono=models.IntegerField()

class Usuario(models.Model):
    idUsuario=models.IntegerField(primary_key=True)
    tipoDeUsuario=models.CharField(max_length=30)
    password=models.CharField(max_length=55)

class OrdenDeCompra(models.Model):
    idOrdenDeCompra=models.IntegerField(primary_key=True)
    nit=models.IntegerField()
    idProducto=models.IntegerField()

class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True)#, default="", editable=False)
    idEmpresaFarmaceutica=models.IntegerField()
    idPresentacion=models.IntegerField()
    Estante=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    precio=models.FloatField()
    cantidad=models.IntegerField()
    productoMainImg = models.ImageField(upload_to='productos/')

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.productoMainImg.url))
    image_tag.short_description = 'Image'

class EmpresaFarmaceutica(models.Model):
    idEmpresaFarmaceutica=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    pais=models.CharField(max_length=30)

class Presentacion(models.Model):
    idPresentacion=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
       
class Proveedor(models.Model):
    idProveedor=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()
    email=models.EmailField(blank=True, null=True)

class Producto_has_Proveedor(models.Model):
    idProducto_has_Proveedor=models.IntegerField(primary_key=True)
    idProducto=models.IntegerField()
    idProveedor=models.IntegerField()


