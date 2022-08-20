'''sueldo_ingresado = input("ingrese su sueldo")
sueldo_acumulado = 0
cantidad_sueldos = 0
detalle_sueldos = []


while int(sueldo_ingresado) > 0:
    detalle_sueldos.append(sueldo_ingresado)
    sueldo_acumulado = sueldo_acumulado + int(sueldo_ingresado)
    cantidad_sueldos = cantidad_sueldos + 1
    print("sueldo ingresado"+ str(sueldo_ingresado))
    sueldo_ingresado = input("ingrese su sueldo")

print("sueldo acumulado "+ str(sueldo_acumulado))
print("cantidad sueldos ingresados "+ str(cantidad_sueldos))
print("sueldo promedio "+ str(sueldo_acumulado/cantidad_sueldos))
print(detalle_sueldos)
    '''