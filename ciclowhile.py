
"""
i = 1
while i < 10: 
    print("holamundo")
    print("Esta es la vuelta mundo",i)
    i = i + 1
"""

"""
Tabla = int(input("Que tabla quiere: "))
i = 1 
while i <= 10:
    x = i * Tabla
    print(Tabla, "x", i, "=",x)
    i = i + 1

"""
"""
multiplos_del_7 = []
for numero in range(1,101):
    if numero %7 == 0:
        multiplos_del_7.append(numero)
print(multiplos_del_7)
    
"""

def encontrar_multiplos(limite_superior=100):
    """
    Encuentra los múltiplos de un número especificado por el usuario
    dentro de un rango de 1 hasta el límite_superior.
    """
    while True:
        try:
            # Solicitar al usuario el número del cual quiere los múltiplos
            numero_multiplo = int(input("Ingresa el número del cual quieres encontrar los múltiplos: "))

            # Validar que el número no sea cero para evitar divisiones por cero o bucles infinitos
            if numero_multiplo == 0:
                print("No puedes encontrar múltiplos de cero (o el resultado serían todos los números). Por favor, ingresa un número diferente de cero.")
                continue # Pide el número de nuevo
            break # Sale del bucle si el número es válido

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    multiplos_encontrados = []
    # Iterar desde 1 hasta el límite superior (incluyéndolo)
    for numero in range(1, limite_superior + 1):
        # Si el residuo de la división es 0, es un múltiplo
        if numero % numero_multiplo == 0:
            multiplos_encontrados.append(numero)

    # Mostrar los resultados
    if multiplos_encontrados:
        print(f"\nLos múltiplos de {numero_multiplo} del 1 al {limite_superior} son:")
        print(multiplos_encontrados)
    else:
        print(f"\nNo se encontraron múltiplos de {numero_multiplo} del 1 al {limite_superior}.")

# Llamar a la función para ejecutar el programa
encontrar_multiplos(100)


           



    


