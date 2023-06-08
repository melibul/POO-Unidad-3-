from clase_manejafacultad import *
if __name__ == '__main__':
	manejador=ManejaFacultades()
	manejador.leerArchivo()
	opc=None
	while(opc!=0):
		print('\t\t\t\t\t\t\t\t\t\t\t\t---MENU DE OPCIONES---')
		print('1.  Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.')
		print('2. Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.')
		print('0. Terminar y cerrar programa.\n\n\t\t\t')
		opc=int(input('Ingrese opcion: '))

		if opc==1:
			codigo=input('Ingrese codigo de facultad:\n')
			manejador.mostrar(codigo)
		elif opc==2:
			nombre=input('Ingrese nombre de la carrera\n')
			manejador.recorreFac(nombre)
print('adiosito vuelva pronto<3')