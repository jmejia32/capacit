#encoding:utf-8
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from capacit.models import *
from capacit.forms import *
# Create your views here.

def inicio(request):
	return render(request, "ejemplo.html", {})


def modifcapacit(request):
	pass


def agrcapacit(request):
	if request.method == 'POST':
		formulario = CapacitacionForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return render(request, "ejemplo.html", {'msj':'La capacitación se registró correctamente'})
		else:
			formulario = CapacitacionForm()
			return render(request, "agrcapacit.html", {'err':'Complete todos los campos', 'formulario':formulario})
	else:
		formulario = CapacitacionForm()
		return render(request, "agrcapacit.html",{'formulario':formulario})


def elimcapacit(request):
	pass


def trabencapacit(request):
	pass


def notrabencapacit(request):
	pass


def login(request):
	pass


def salir(request):
	pass


def agrtrab(request):
	if request.method == 'POST':
		formulario = TrabajadorForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return render(request, "ejemplo.html", {'msj':'El trabajador se ha guardado correctamente'})
		else:
			formulario = TrabajadorForm()
			return render(request, "agrtrab.html", {'err':'Complete todos los campos', 'formulario':formulario})
	else:
		formulario = TrabajadorForm()
		return render(request, "agrtrab.html", {'formulario':formulario})