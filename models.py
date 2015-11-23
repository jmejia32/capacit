from django.db import models


class Trabajador(models.Model):
	cc = models.CharField(max_length=20, primary_key=True)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)


	def getCC(self):
		return self.cc


	def getNombre(self):
		return self.nombre


	def getApellido(self):
		return self.apellido


	def setCC(self, ncc):
		self.cc = ncc


	def setNombre(self, nnom):
		self.nombre = nnom


	def setApellido(self, nape):
		self.apellido = nape


	def __str__(self):
		return self.nombre+" "+self.apellido


class Capacitacion(models.Model):
	nombre = models.CharField(max_length=50)
	descrip = models.CharField(max_length=100)
	fechaI = models.DateField()
	fechaF = models.DateField()
	tutor = models.CharField(max_length=50)


	def getNombre(self):
		return self.nombre


	def setNombre(self, nnom):
		self.nombre = nnom


	def getDescrip(self):
		return self.descrip


	def setDescrip(self, ndsc):
		self.descrip = ndsc


	def getFechaI(self):
		return self.fechaI


	def setFechaI(self, nfi):
		self.fechaI = nfi


	def getFechaF(self):
		return self.fechaF


	def setFechaF(self, nff):
		self.fechaF = nff


	def getTutor(self):
		return self.tutor


	def setTutor(self, ntut):
		self.tutor = ntut


	def __str__(self):
		return self.nombre


class Asignacion(models.Model):
	idTrab = models.ForeignKey('Trabajador', related_name='Trabajador')
	idCapacit = models.ForeignKey('Capacitacion', related_name='Capacitacion')


	def getIDTrab(self):
		return self.idTrab


	def setIDTrab(self, idt):
		self.idTrab = idt


	def getIDCapacit(self):
		return self.idCapacit


	def setIDCapacit(self, idc):
		self.idCapacit = idc


	def __str__(self):
		return self.idTrab+" en "+self.idCapacit