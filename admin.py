from django.contrib import admin
from capacit.models import *


class TrabajadorAdmin(admin.ModelAdmin):
	list_display = ('cc','nombre','apellido')


class CapacitacionAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','descrip','fechaI','fechaF','tutor')


class AsignacionAdmin(admin.ModelAdmin):
	list_display = ('id','idTrab','idCapacit')


admin.site.register(Trabajador,TrabajadorAdmin)
admin.site.register(Capacitacion,CapacitacionAdmin)
admin.site.register(Asignacion, AsignacionAdmin)