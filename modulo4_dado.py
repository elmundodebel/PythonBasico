'''Ejercicio 2
Dado
Generar un programa de consola que tenga un
menú y permita generar números aleatorios
entre 1 y 6, como si fuera un dado.
Menú
1. Tirar dado.
2. Salir
'''


import random


def tirar_dado():
    print(random.randint(1,6))


opcion = input("Ingrese la opcion deseada\n    1. Tirar dado. \n    2. Salir\n    Opcion: ")

while True:
    while opcion.isdecimal() == True:
        while int(opcion) ==1:
            tirar_dado()
            opcion = input("Ingrese la opcion deseada\n    1. Tirar dado. \n    2. Salir\n    Opcion: ")
    opcion = input("Ingrese la opcion deseada\n    1. Tirar dado. \n    2. Salir\n    Opcion: ")

