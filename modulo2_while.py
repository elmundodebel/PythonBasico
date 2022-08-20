'''
a = 1
b = 1
while(a<5):
    print("a es menor que 5. Es "+ str(a))
    a = a+1
'''


'''
#laboratorioo ejericio 1
a = 1
while(a<10):
    print(str(a))
    a = a+1
'''


name = input("Por favor ingrese su nombre")

#while name == '':
while len(name.strip()) == 0:
    print("Error. El nombre ha sido ingresado incorrrectamente")
    name = input("Por favor ingrese su nombre")

print("Bienvenido "+name)
