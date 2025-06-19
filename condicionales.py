
"""
horas = int(input("Horas trabajadas: "))
Valorhora = int(input("Cuanto gana por hora: "))
Valorapagar = horas * Valorhora
#Vamos a dar subsidio de 200K a los que ganes menos de 1.5M

if Valorapagar < 1500000: 
    Valorapagar += 200000 
else:
    Valorapagar +=100000
print("El valor a recibir es: ",Valorapagar)
"""

Edad = int(input("Ingrese la edad: "))

if Edad <= 0:
        print("ERROR")
elif Edad >= 6 and Edad < 18:
    print("Adolecencia")
elif Edad >= 18 and Edad < 25:
     print("Adulto")
elif Edad > 125:
     print("ERROR")

else:
    print("Adulto")



