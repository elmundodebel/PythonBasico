'''Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares.
'''
enero_a_junio = 300
julio_a_octubre = 500
noviembre_a_diciembre = 700

sueldo_promedio = round((enero_a_junio*6+julio_a_octubre*4+noviembre_a_diciembre*2)/12)
print("El sueldo promedio fue "+str(sueldo_promedio))


#FORMA 1
print("forma1")
if sueldo_promedio > 900:
    print("Su sueldo es mejor de lo normal")
elif sueldo_promedio > 300:
    print("Su sueldo es normal")
else:
    print("Su sueldo es bajo")



print("")

#FORMA2
print("forma2")
if sueldo_promedio < 300:
    print("Tiene Sueldo Bajo")
elif sueldo_promedio>= 300 and sueldo_promedio <=900:
    print("Tiene sueldo normal")
else:
    print("Tiene sueldo bajo")






