import csv
from clase_facultad import *
class ManejaFacultades():
	def __init__(self):
		self.__manejador=[]
	def leerArchivo(self):
		archivo=open('Facultades.csv', encoding='utf8')
		reader=csv.reader(archivo,delimiter=',')
		for fila in reader:
			if len(fila)==5:
				unafacultad=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
				self.__manejador.append(unafacultad)
			else:
				unafacultad.agregar_carrera(fila)
	def buscar_cod(self, cod):
		i=0
		band=False
		retorno=None
		while i<len(self.__manejador) and not band:
			if(self.__manejador[i].getCod()==cod):
				band=True
				retorno=i
			else:
				i=i+1
		return retorno
	def mostrar(self,cod):
		i=self.buscar_cod(cod)
		if(i==None):
			print('El codigo de facultad no existe')
		else:
			self.__manejador[i].mostrar_nomb()
			self.__manejador[i].mostrar_carr()

	def mostrar2(self, codigo,i):
		print('Codigo: {}'.format(str(self.__manejador[i].getCod())+str(codigo)))
		self.__manejador[i].mostrar_nomb()
		print('Localidad: {}'.format(self.__manejador[i].getLoc()))

	def recorreFac(self, nombre):
		i=0
		band=False
		while not band and i<len(self.__manejador):
			b=self.__manejador[i].busca_fac(nombre)
			if(b!=None):
				self.mostrar2(b,i)
				band=True
			i=i+1