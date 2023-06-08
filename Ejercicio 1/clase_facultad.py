import csv
from clase_carrera import *
class Facultad():
	__codigo=''
	__nombre=''
	__direccion=''
	__localidad=''
	__telefono=''
	__carrera:list
	def __init__(self,cod,nomb,direc,loc,tel):
		self.__codigo=cod
		self.__nombre=nomb
		self.__direccion=direc
		self.__localidad=loc
		self.__telefono=tel
		self.__carrera=[]
	def agregar_carrera(self, fila):
		unacarrera = carrera(fila[1],fila[2],fila[3],fila[4],fila[5])
		self.__carrera.append(unacarrera)
	def getCod(self):
		return self.__codigo
	def getLoc(self):
		return self.__localidad
	def mostrar_nomb(self):
		print('Nombre de facultad:', self.__nombre)
	def mostrar_carr(self):
		for carrera in self.__carrera:
			carrera.mostrar_dur()
	def buscar_nombre(self, nomb):
		i=0
		band=False
		retorno=None
		while not band and i<(len(self.__carrera)):
			if self.__carrera[i].get_nomb()==nomb:
				retorno=i
				band=True
			else:
				i=i+1
		return retorno
	def busca_fac(self, nombre):
		i=0
		band=False
		retorno=None
		while not band and i<(len(self.__carrera)):
			if self.__carrera[i].get_nomb()==nombre:
				retorno=i+1

				band=True
			else:
				i=i+1
		return retorno