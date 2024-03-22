# Generador de passwords simple v1.0 

import string
import random

longitud = int(input("Ingrese la longitud de la password: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: " + contrasena)
