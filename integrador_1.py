'''Etapa 1
Una universidad desea crear un programa para
contabilizar los cursos que tiene cada alumno.
Para ello se debe realizar primero una aplicación
de consola la cual debe solicitar el nombre de un
alumno y la cantidad de cursos en la que se
encuentra inscripto.
Estos dos valores deben almacenarse como una
lista de dos elementos (el nombre y la cantidad
de cursos como un número entero) en una lista
de alumnos'''


listado = [["Alumno","Cantidad de cursos"]]

print(listado[len(listado)-1])

def ingreso_registro():
    name = input("Por favor ingrese su nombre: ")
    cant_cursos= input("Ingrese la cantidad de cursos a los cuales se encuentra inscripto: ")
    listado.append([name,cant_cursos])
    print(listado[len(listado)-1])
    

def mostrar_listado():
    for element in listado:
        print(element)

def exit():
    print("Programa finalizado")


def programa():
    opcion = int(input("Ingrese el numero de la opcion deseada \n   1. Agregar un nuevo alumno \n   2. Ver listado de alumnos\n   3. Salir\n"))
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
        exit()

programa()

