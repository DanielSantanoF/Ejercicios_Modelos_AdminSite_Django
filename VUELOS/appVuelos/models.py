from django.db import models

# Create your models here.
from django.utils.timezone import now


class Aeropuerto(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    ciudad = models.CharField('Ciudad', max_length=50)
    siglas = models.CharField('Siglas', max_length=3)

    def __str__(self):
        return 'Aeropuerto %s de la ciudad de %s tiene las siglas %s' % (self.nombre, self.ciudad, self.siglas)


class Vuelo(models.Model):
    aeropuerto_salida = models.ForeignKey(Aeropuerto, related_name='AeropuertoDeSalida', on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField('Fecha de salida', default=now)
    aeropuerto_llegada = models.ForeignKey(Aeropuerto, related_name='AeropuertoDeLlegada', on_delete=models.CASCADE)
    fecha_llegada = models.DateTimeField('Fecha de llegada', default=now)

    def __str__(self):
        return 'El vuelo %s - %s saldra el %s con llegada el %s' % (self.aeropuerto_salida, self.aeropuerto_llegada, self.fecha_salida, self.fecha_llegada)


class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    email = models.CharField('Email', max_length=50)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento', default=now)

    def __str__(self):
        return 'Cliente %s %s con email %s nacio el %s' % (self.nombre, self.apellidos, self.email, self.fecha_nacimiento)


class Reserva(models.Model):
    vuelo = models.ForeignKey(Vuelo, related_name='VueloDeCliente', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='DatosDeCliente', on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField('Fecha de la reserva', default=now)
    precio = models.IntegerField('Precio', default=80)

    def __str__(self):
        return 'La reserva del cliente %s para el vuelo %s del %s tiene un precio de %s' % (self.cliente, self.vuelo, self.fecha_reserva, self.precio)