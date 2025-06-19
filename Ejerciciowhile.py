def simular_restaurante():
    """
    Simula un restaurante: muestra un menú, permite al cliente pedir
    y calcula el total de la factura.
    """
    menu = {
        "1": {"nombre": "Hamburguesa Clásica", "precio": 12.50},
        "2": {"nombre": "Pizza Pepperoni", "precio": 15.00},
        "3": {"nombre": "Ensalada César", "precio": 9.75},
        "4": {"nombre": "Pasta Carbonara", "precio": 13.25},
        "5": {"nombre": "Tacos al Pastor (3)", "precio": 11.00},
        "6": {"nombre": "Refresco", "precio": 2.50},
        "7": {"nombre": "Agua Mineral", "precio": 2.00},
        "8": {"nombre": "Postre de Chocolate", "precio": 6.00}
    }

    orden_cliente = {} # Aquí guardaremos lo que el cliente pida
    total_cuenta = 0.0

    print("¡Bienvenido a nuestro restaurante!")
    print("--- Nuestro Menú ---")

    # Mostrar el menú al cliente
    for key, item in menu.items():
        print(f"{key}. {item['nombre']}: ${item['precio']:.2f}")
    print("--------------------")

    # Tomar el pedido del cliente
    while True:
        eleccion = input("Ingresa el número del platillo que deseas (o 'fin' para terminar tu pedido): ").lower()

        if eleccion == 'fin':
            break
        elif eleccion in menu:
            while True:
                try:
                    cantidad = int(input(f"¿Cuántas unidades de '{menu[eleccion]['nombre']}' deseas? "))
                    if cantidad > 0:
                        # Añadir al pedido del cliente
                        if eleccion in orden_cliente:
                            orden_cliente[eleccion]['cantidad'] += cantidad
                        else:
                            orden_cliente[eleccion] = {"nombre": menu[eleccion]['nombre'], "precio": menu[eleccion]['precio'], "cantidad": cantidad}
                        print(f"'{menu[eleccion]['nombre']}' añadido a tu pedido.")
                        break # Sale del bucle de cantidad
                    else:
                        print("Por favor, ingresa una cantidad positiva.")
                except ValueError:
                    print("Cantidad inválida. Ingresa un número entero.")
        else:
            print("Número de platillo no válido. Por favor, elige un número del menú o escribe 'fin'.")

    # Generar la factura
    print("\n--- TU FACTURA ---")
    if not orden_cliente:
        print("No has pedido nada. ¡Vuelve pronto!")
    else:
        for key, item_ordenado in orden_cliente.items():
            subtotal = item_ordenado['precio'] * item_ordenado['cantidad']
            total_cuenta += subtotal
            print(f"{item_ordenado['nombre']} x {item_ordenado['cantidad']} = ${subtotal:.2f}")

        print(f"--------------------")
        print(f"TOTAL A PAGAR: ${total_cuenta:.2f}")
        print("¡Gracias por tu visita!")

# Ejecutar la simulación del restaurante
simular_restaurante()