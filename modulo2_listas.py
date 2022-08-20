nombre1="Mai"
nombre2="Belu"
nombre3="Nico"

nombres = {"Mai","Belu","Nico"}

print(nombres)

datos= ["Mai",32,"Buenos Aires","Bibliotecaria","Python"]


#acceder a un dato especifico, ej elemento 2
print("ejemplo acceder a un elemento")
print(datos[2])

#contar elementos
print("ejemplo contar elementos")
print(len(datos))

for element in datos:
    print(element)

#Agregar elementos en la lista, pero en una sola ubicacion. solo admite un argumento
print("ejemplo append")
datos.append(['prueba','append'])
for element in datos:
    print(element)

#Agregar elementos en la lista. en vaarios elementos. admite varios argumentos
print("ejemplo extend")
datos.extend(['prueba','append'])
for element in datos:
    print(element)

datos.extend(['Python'])

#ubicar un elemento, que nos de la posicion de donde esta. solo nos da la primera
print("ejemplo index")
print(datos.index('Python'))

#cuenta cuantas veces aparece un valor
print("ejemplo count")
print(datos.count('Python'))

#insert agregar un nombre en una ubicacion especifica
print("lista original")
nombres = ['Susana','Alejandro','Roberto']
for element in nombres:
    print(element)

nombres.insert(2,'Paula')

nombres.extend(['Silvina'])
print("lista modificada")

for element in nombres:
    print(element)


a = [1]
while (a<101):
    a.extend([1+a])
