"""

def mostrar_tablas_de_multiplicar():
    for i in range (1,11):
        print(f"---Tabla del {i}---")
        for j in range(1,11):
            print(f"{i}x{j} = {i * j}")
            print()
mostrar_tablas_de_multiplicar()
"""

def mostrar_tablas_con_while():
    """
    Muestra las tablas de multiplicar del 1 al 10 usando bucles while.
    """
    i = 1  # Inicializamos el contador para la tabla de multiplicar (la tabla del 1)

    while i <= 10:  # El bucle exterior se ejecutará mientras i sea menor o igual a 10
        print(f"--- Tabla del {i} ---")
        
        j = 1  # Inicializamos el contador para el multiplicador (comienza en 1)
        # Es crucial reiniciar 'j' a 1 en cada iteración del bucle exterior.
        
        while j <= 10:  # El bucle interior se ejecutará mientras j sea menor o igual a 10
            print(f"{i} x {j} = {i * j}")
            j += 1  # Incrementamos 'j' para pasar al siguiente número (2, 3, 4...)
        
        print()  # Línea en blanco para separar las tablas
        i += 1  # Incrementamos 'i' para pasar a la siguiente tabla (del 2, del 3, etc.)

# Llama a la función para mostrar las tablas
mostrar_tablas_con_while()