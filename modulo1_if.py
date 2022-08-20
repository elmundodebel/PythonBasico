
edad = 5
tiene_sobrepeso = 1

if edad>18:
    print("Es mayor de edad")
elif edad < 18 and not(tiene_sobrepeso == 1):
    print("Niño gordo")
elif edad == 18:
    print("Tiene 18 años")
else:
    print("Es menor de edad")