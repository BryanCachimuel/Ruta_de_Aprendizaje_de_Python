"""
Formato de cadena
"""

# %s -> string   %d -> enteros  %.2f -> indica la cantidad de decimales va a tener este double
nombre = "Lennin"
edad = 30
estatura = 1.52

mensaje = "Hola, me llamo %s, tengo %d años y mido %.2f metros" % (nombre, edad, estatura)

# para formatear el decimal se pone el formato {:.2f}
mensaje_formato = "Hola, me llamo {}, tengo {} años y mido {:.2f} metros" .format(nombre, edad, estatura)

# otra forma de formatear
mensaje_formato_string = f"Hola, me llamo {nombre}, tengo {edad} años y mido {estatura:.2f} metros"

print(mensaje)
print(mensaje_formato)

