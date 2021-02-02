from django.contrib import admin
from .models import Pildora, Cliente, Empleado, Usuario, OrdenDeCompra, EmpresaFarmaceutica, Presentacion, Producto, Producto_has_Proveedor, Proveedor

class ProductoAdmin(admin.ModelAdmin):
    search_fields=['nombre']
    list_display = ('idProducto' ,'productoMainImg', 'image_tag', 'precio', 'cantidad', )
    list_filter=['precio']


admin.site.register(Pildora)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(OrdenDeCompra)
admin.site.register(EmpresaFarmaceutica)
admin.site.register(Presentacion)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Producto_has_Proveedor)
admin.site.register(Proveedor)