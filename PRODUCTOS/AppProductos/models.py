from django.db import models
from AppProductos.utils import image_upload_location


# Create your models here.

class Categoria_Padre(models.Model):
    nombre = models.CharField('Nombre de categoria', max_length=50, default='Nombre de categoria')

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField('Nombre de categoria', max_length=50, default='Nombre de categoria')
    categoria_padre = models.ForeignKey(Categoria_Padre, blank=True, null=True, related_name="categoriaPadre", on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField('Nombre de producto', max_length=50, default='Nombre de producto')
    descripcion = models.TextField(max_length=1000, help_text='Descripción del producto')
    url_imagen = models.ImageField("Image", blank=True, null=True, upload_to=image_upload_location)
    precio_unidad = models.DecimalField('Precio', max_digits=6, decimal_places=2, default=0)
    categoria = models.ManyToManyField(Categoria, help_text="Seleccione una categoria para este producto")

    # models.ForeignKey(Categoria, blank=True, related_name="categoria", on_delete=models.CASCADE)

    def __str__(self):
        return 'Producto %s con descripcion: %s, de la caterogia %s tiene un precio de: %s' % (
        self.nombre, self.descripcion, self.categoria, self.precio_unidad)

    def lista_categorias(self):
        return ', '.join([categoria.nombre for categoria in self.categoria.all()[:1]])

    lista_categorias.short_description = 'Categoria'
