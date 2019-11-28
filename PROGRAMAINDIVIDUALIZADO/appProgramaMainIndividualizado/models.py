from django.db import models

# Create your models here.
from django.utils.timezone import now


class Residente(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=100)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True, default=now)

    def __str__(self):
        return 'Residente: %s %s nacio el %s' % (self.nombre, self.apellidos, self.fecha_nacimiento)


class Familiar(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=100)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True, default=now)
    parentesco = models.ForeignKey(Residente, related_name='familiarResidente', on_delete=models.CASCADE)

    def __str__(self):
        return 'Familiar de %s es %s %s que nacio el %s' % (self.parentesco, self.nombre, self.apellidos, self.fecha_nacimiento)


class ParteInforme(models.Model):
    TIPO_PARTE = (
        ('sa', 'SANTIARIA'),
        ('fu', 'FUNCIONAL'),
        ('ps', 'PSIQUICA'),
        ('so', 'SOCIAL'),
        ('te', 'TERAPIA '),
        ('oc', 'OCUPACIONAL'),
    )

    tipo = models.CharField(max_length=2, choices=TIPO_PARTE, blank=True, default='fu', help_text='Tipo de parte')
    valoracion_inicial = models.IntegerField('Valoracion inicial', default=now, blank=True)
    objetivos = models.TextField(max_length=1000, help_text='Objetivos')
    informe = models.TextField(max_length=1000, help_text='Informe')

    def __str__(self):
        return 'La parte de informe de tipo %s tiene una valoracion inicial de %s en el informe se trata %s y su objetivo es %s' % (self.tipo, self.valoracion_inicial, self.informe, self.objetivos)


class Informe(models.Model):
    fecha_informe = models.DateField('Fecha del informe', blank=True, default=now)
    # partes = models.ForeignKey(ParteInforme, related_name='parteDeInforme', on_delete=models.SET_NULL)
    partes = models.ManyToManyField(ParteInforme, related_name='partesDelInforme', help_text="Selecciona las partes del informe")

    def __str__(self):
        return 'El informe consta de la(s) parte(s) %s y fue realizado en %s' % (self.partes, self.fecha_informe)

    def lista_partes_informe(self):
        return ', '.join([partes.tipo for partes in self.partes.all()[:1]])

    lista_partes_informe.short_description = 'Partes del informe'