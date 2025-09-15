"""
EL programa determina si una palabra comiena con cualquier vocal 
"""

# Declaraciones

# Entradas
palabra = input("Introduce una palabra: ")

# Proceso
vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
if palabra and palabra[0] in vocales:
    mensaje = f"'{palabra}' comienza con vocal"
else:
    mensaje = f"'{palabra}' no comienza con vocal"

# Salidas
print(mensaje)