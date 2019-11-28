from django.contrib import admin

# Register your models here.
from .models import Residente, Familiar, ParteInforme, Informe

admin.site.register(Residente)
admin.site.register(ParteInforme)


@admin.register(Familiar)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento', 'parentesco')

@admin.register(Informe)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('fecha_informe', )
