#encoding:utf-8
from django import forms
from django.forms import ModelForm
from capacit.models import *

class DateInput(forms.DateInput):
	input_type = "date"


class TrabajadorForm(ModelForm):
	class Meta:
		model = Trabajador
		fields = ('cc','nombre','apellido')
		labels = {
			'cc': 'Cédula de Ciudadanía',
			'nombre': 'Nombre',
			'apellido': 'Apellido'
		}
		widgets = {
			'cc': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'})	
		}


class CapacitacionForm(ModelForm):
	class Meta:
		model = Capacitacion
		fields = ('nombre', 'descrip', 'fechaI','fechaF','tutor')
		labels = {
			'nombre':'Nombre de la Capacitación', 
			'descrip':'Descripción', 
			'fechaI':'Fecha de Inicio',
			'fechaF':'Fecha de Finalización',
			'tutor':'Nombre del Tutor'
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
			'descrip': forms.TextInput(attrs={'class': 'form-control'}), 
			'fechaI': DateInput(attrs={'class': 'form-control'}),
			'fechaF': DateInput(attrs={'class': 'form-control'}),
			'tutor': forms.TextInput(attrs={'class': 'form-control'})
		}


class AsignacionForm(ModelForm):
	class Meta:
		model = Asignacion
		fields = ('idTrab','idCapacit')
		labels = {
			'idTrab':'Seleccione un Trabajador',
			'idCapacit':'Seleccione una Capacitación'
		}
		widgets = {
			'idTrab': forms.Select(attrs={'class': 'form-control'}),
			'idCapacit': forms.Select(attrs={'class': 'form-control'})
		}