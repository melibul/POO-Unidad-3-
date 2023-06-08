import csv
class carrera():
	__codigo=''
	__nombre=''
	__fecha_inicio=''
	__duracion=''
	__titulo=''
	def __init__(self,cod, nomb,fecha,dur,tits):
		self.__codigo=cod
		self.__nombre=nomb
		self.__fecha_inicio=fecha
		self.__duracion=dur
		self.__titulo=tits
	def mostrar_dur(self):
		print('Nombre de la carrera: {}'.format(self.__nombre))
		print('Duracion: {}'.format(self.__duracion))
	def get_nomb(self):
		return self.__nombre
	def get_cod(self):
		return self.__codigo 





