'''matriz = [[3.3,6.1,4.0],[4.9, 5.7, 6.4]]


fila = input("Que fila desea?")
columna = input("Que columna desea?")
print(matriz[1][2])
print(matriz[int(fila)-1][int(columna)-1])
print(matriz[1][2])

Crear un programa que solicite una fila y una
columna e imprima en pantalla el número en
esa posición según la siguiente matriz:
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

Un ejemplo de entrada (lo que escribe el
usuario) y salida (lo que se imprime en
pantalla) es el siguiente (los caracteres
en azul son ingresados por el usuario):
Fila: 1
Columna: 2

6.4
El resultado es 6.4 puesto que es el valor
ubicado en matriz[1][2].'''



matriz = [[3.3,6.1,4.0],[4.9, 5.7, 6.4]]
#consultar fila
fila = input("Que fila desea?")
while int(fila) > 2:
    fila=input("Error! La matriz contiene solo 2 filas.Que fila desea? ")
#consultar columna
columna = input("Que columna desea?")
while int(columna) > 3:
    columna =input("Error! La matriz contiene solo 3 columnasQue columna desea? ")
print(matriz[int(fila)-1][int(columna)-1])

