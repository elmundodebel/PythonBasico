print("Ingrese el numero de operaiones que desea realizar: ")
print("1. Ver lista de alumnos")
print("2.Añadir un Alumno a la lista")
print("3.salir")
operacion = input(">>> ")

operaciones = [1, 2, 3]

numero_operacion = int(operacion)

alumno_curso = [["Pablo Acevedo", 3], ["Juan Perez", 2], ["Pedro Pérez", 1]]

if numero_operacion in operaciones:
    if numero_operacion == 1:
        print("Lista de alumnos: " + str(alumno_curso))

    elif numero_operacion == 2:
        print("Añadir un Alumno a la lista: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        curso = input("Ingrese cantidad de curso: ")
        alumno_curso.append([nombre + " " + apellido, curso ])
        print(alumno_curso)
    elif numero_operacion == 3:
        print("Gracias por usar el programa")

    else:
        print("Operacion no valida")
