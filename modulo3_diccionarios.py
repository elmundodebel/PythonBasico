#Colecciones: listas, tuplas, diccionarios
#una lista es un conjunto ordenado de datos, utilizandose un indice
alumnos_lista = ["Juan","Sofia","Pablo"]

print("en los diccionarios utilizo clave para acceder al registro, no index. va antes de cada elemento luego dos puntos")
# le invento 123 como dni, 456 y 789.
alumnos_diccionario = {123:"Juan", 456:"Sofia", 789:"Pablo"}
print(alumnos_diccionario)
print("\n")

print("consulto el registro 123, que es la clave para entrar")
print(alumnos_diccionario[123])
print("\n")

print("borro el registro 456")
del alumnos_diccionario[456]
print(alumnos_diccionario)
print("\n")

print("agrego un registro")
alumnos_diccionario[321] = "Mariano"
print(alumnos_diccionario)
print("\n")

print("modificio el registro 123")
alumnos_diccionario[123] = "Juan Cruz"
print(alumnos_diccionario)
print("\n")

print(len(alumnos_diccionario))