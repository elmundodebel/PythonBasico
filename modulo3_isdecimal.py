'''Ejercicio 1
Forzar el ingreso numérico.
Crear un programa que pida un número, verificar
que ese ingreso por input sea un número posible
de convertir a entero. En caso contrario volver a
pedir el ingreso.'''

edad = input("ingrese su edad ")
while edad.isdecimal() == False:
    edad = input("Error! ingrese su edad solo con valores númericos ")

print("Su edad fue ingresada correctamente")