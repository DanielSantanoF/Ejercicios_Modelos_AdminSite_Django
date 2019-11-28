# Generated by Django 2.2.7 on 2019-11-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProductos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='categoria_padre',
        ),
        migrations.AddField(
            model_name='categoria',
            name='categoria_padre',
            field=models.ManyToManyField(help_text='Seleccione una categoria', related_name='categoriaPadre', to='AppProductos.Categoria'),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(help_text='Seleccione una categoria para este producto', to='AppProductos.Categoria'),
        ),
    ]