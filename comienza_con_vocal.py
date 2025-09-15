"""
EL programa determina si una palabra comiena con cualquier vocal 
"""

# Declaraciones


# Entradas
palabra = input("Introduce una palabra: ")

# Proceso
if palabra[0] in "aeiou":
    mensaje = f"'{palabra}' comienza con vocal"
else:
    mensaje = f"'{palabra}' no comienza con vocal"

# Salidas
print(mensaje)