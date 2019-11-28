from django.contrib import admin

# Register your models here.
from .models import Aeropuerto, Vuelo, Cliente, Reserva

admin.site.register(Aeropuerto)
admin.site.register(Vuelo)
admin.site.register(Cliente)
admin.site.register(Reserva)
