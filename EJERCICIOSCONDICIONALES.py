
horas = int(input("Horas trabajadas: "))
Valorhoras = int(input("Ingresa cuanto ganas por hora"))
genero = str(input("Indique cual es su genero (hombre/mujer): ")).strip().lower()
Valorapagar = horas * Valorhoras
F = "mujer"
M = "hombre"
if Valorapagar < 1500000:
    if genero == "mujer":
        Valorapagar += 200000
elif genero == "hombre":
    Valorapagar += 100000

if Valorapagar >1500000 and Valorapagar <2000000:
    Valorapagar +=50000

else:
    Valorapagar >= 2000000
    Valorapagar += 0
    print("El valor a pagar es de", Valorapagar)


    







    





