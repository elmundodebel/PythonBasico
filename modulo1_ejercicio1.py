'''
Armar una frase con las 3 variables dadas y
mostrarla por pantalla.
Es obligatorio usar las 3 variables, pero también
podés agregar palabras vos para generar una
frase. No importa el orden que elijas para las
variables.
'''

textoUno = "Hola"
textoDos = "Buenos Dias"
textoTres = "Buenas Noches"

#print(textoUno + textoDos)

#print(textoUno + textoTres)

horario = 21
if horario >= 20:
    print(textoUno + " " + textoTres)
else:
    print(textoUno + " " + textoDos)