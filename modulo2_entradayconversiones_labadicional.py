'''Ejercicio 1
Comparar la entrada del usuario
Crear un programa que permita ingresar dos
cadenas vía la consola y luego las compare,
imprimiendo un mensaje en caso que sean
iguales y otro en caso que sean diferentes.'''

nombre1= input("Como es tu nombre? ")
nombre2= input("Como es el nombre de tu mama? ")
if nombre1 == nombre2:
    print("Tu mama y vos se llaman igual")
else:
    print("Tu mama y vos se llaman distinto")

'''
Python para no programadores
Ejercicio 2
Pedir nombre
Crear un programa que solicite el nombre de un
alumno a través de la consola, y luego chequee
que no esté vacío.
En caso de estarlo, tiene que imprimir un mensaje
de error; caso contrario, deberá imprimir un men-
saje indicando que se ingresó correctamente.
'''

name = input("Por favor ingrese su nombre ")

if name == '':
    print("Error. El nombre ha sido ingresado incorrrectamente")
else:
    print("El nombre ha sido ingresado corrrectamente")

#strip  sirve para sacarle los espacios adelante y atras 
#name = name.strip()
# el len() sirve para decir el largo
#print(len(name.strip()))

if len(name.strip()) == 0:
    print("Error. El nombre ha sido ingresado incorrrectamente")
else:
    print("El nombre ha sido ingresado corrrectamente")

#edad = input("Cual es tu edad?")


'''
Ejercicio 3
Comparar entrada de números
Pedir la edad por teclado y comparar si es
mayor o menor de edad. No olvidar de que para
poder comparar el ingreso debe ser convertido a
int, ya que el usuario ingresa un número entero.
'''

edad = input("cual es la edad?")
if int(edad)>= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")