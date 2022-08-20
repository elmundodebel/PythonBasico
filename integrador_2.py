'''Etapa 1
La lista de alumnos que creamos en el módulo
anterior ahora debe ser un diccionario, en donde
las claves serán nombres de alumnos y los
valores sus respectivas cantidades de cursos.
Para esto se debe modificar el código de las
opciones 1 y 2 (agregar un nuevo alumno y ver la
lista de alumnos).
La tercera opción será “Ver la cantidad de cursos
de un alumno”. Deberá solicitar el nombre de un
alumno e imprimir en pantalla el número de
cursos que tiene asociados como clave. La cuarta
opción es la de salir, como en la versión anterior.'''


listado = {"nombre_alumno": "Cantidad de cursos"}

#print(listado[len(listado)-1])

def ingreso_registro():
    name = input("Por favor ingrese su nombre: ")
    cant_cursos= input("Ingrese la cantidad de cursos a los cuales se encuentra inscripto: ")
    listado[name] = cant_cursos
    print(listado[name])
    
def mostrar_listado():
    print(listado)

def exit():
    print("Programa finalizado")


def programa():
    opcion = int(input("Ingrese el numero de la opcion deseada \n   1. Agregar un nuevo alumno \n   2. Ver listado de alumnos\n   3. Ver la cantidad de cursos de un alumno\n   4. Salir\n"))
    while opcion < 0 or opcion > 3:
        print("Opcion inexistente")
        opcion
    if opcion == 1:
        ingreso_registro()
        programa()
    elif opcion ==2:
        mostrar_listado()
        programa()
    elif opcion ==3:
        nombre_alumno = input("Ingrese el nombre del alumno que desea ver los cursos ")
        print(listado[nombre_alumno])
        programa()
    elif opcion ==4:
        exit()

programa()

