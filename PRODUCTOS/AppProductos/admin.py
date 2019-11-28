from django.contrib import admin
from .models import Producto, Categoria, Categoria_Padre


# Register your models here.

@admin.register(Categoria_Padre)
class Categoria_PadreAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria_padre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'url_imagen', 'precio_unidad', 'lista_categorias')
