from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from capacit.models import *
# Create your views here.

def inicio(request):
	return render(request, "ejemplo.html", {})


def modifcapacit(request):
	pass


def agrcapacit(request):
	pass


def elimcapacit(request):
	pass


def salir(request):
	pass


def trabencapacit(request):
	pass


def notrabencapacit(request):
	pass


def login(request):
	pass


def salir(request):
	pass