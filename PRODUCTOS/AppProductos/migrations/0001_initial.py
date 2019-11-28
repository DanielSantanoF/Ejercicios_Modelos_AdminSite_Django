# Generated by Django 2.2.7 on 2019-11-28 18:15

import AppProductos.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Nombre de categoria', max_length=50, verbose_name='Nombre de categoria')),
                ('categoria_padre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoriaPadre', to='AppProductos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Nombre de producto', max_length=50, verbose_name='Nombre de producto')),
                ('descripcion', models.TextField(help_text='Descripción del producto', max_length=1000)),
                ('url_imagen', models.ImageField(blank=True, null=True, upload_to=AppProductos.utils.image_upload_location, verbose_name='Image')),
                ('precio_unidad', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Precio')),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='AppProductos.Categoria')),
            ],
        ),
    ]