multiplosde5 = []
multiplosde3 = []
inicio_rango = int(input("desde que numero inicia el rango"))
fin_rango = int(input("desde que numero termina el rango"))


for numero in range(inicio_rango,fin_rango+1):
    if numero%5 == 0:
        multiplosde5.append([numero])
    if numero%3 == 0:
        multiplosde3.append([numero])

#print(*multiplosde3)
print("Los numeros divisibles por 5 son: ") 
print(*multiplosde5)
#for numero in multiplosde5:
 #   print(numero)
print("Los numeros divisibles por 3 son: ")
print(*multiplosde3)
#for numero in multiplosde3:
#   print(numero)
