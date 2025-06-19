txt = "el hijo de rana rana"
"""
tamaño = len(txt)
print(tamaño)

"""
print(txt.lower())
print(txt.count("r"))
print(txt.index("r"))
x = txt.capitalize() #para poner la primera letra en mayuscula#
print(x)
x = txt.casefold() #método devuelve una cadena donde todos los caracteres están en minúsculas.
print(x)
txt = "hijo"
x = txt.center(45) #método alineará al centro la cadena, utilizando un carácter específico (el espacio es el predeterminado) como carácter de relleno.#
print(x)
x = txt.count("rana") #método devuelve el número de veces que un valor especificado aparece en la cadena.#
print(x)
""""""

x = txt.encode() #método codifica la cadena con la codificación especificada. Si no se especifica ninguna, se utilizará UTF-8.#
print(x)

x = txt.endswith(".") #método devuelve True si la cadena termina con el valor especificado, de lo contrario False.#
print(x)


