"""
Métodos para las cadenas
"""
# Transforma el texto a un formato de tipo título
texto = "saludos cordiales"
print(texto.title())

# Transforma el titulo a mayúsculas
print(texto.upper())

# Transformas a minúsculas
texto_dos = 'HELLO FRIENDS'
print(texto_dos.lower())

# Transformar la primera letra en mayúscula
print(texto.capitalize())

# Contar cuantas veces se repite una palabra en una cadena de texto
contar_texto = """ Te mandamos saludos, especiales por que los saludos son necesarios para para presentarse y saludar a las personas, así que saludos amigos """
print(contar_texto.count("saludos"))

# Indicar la posición de una palabra dentro de una cadena de texto
posicion_caracter = 'Desarrollo de Software'
print(posicion_caracter.find("l"))
print(posicion_caracter.index("S"))

# Para remplazar una palabra por otra dentro de una cadena
# replace remplaza el primer parámetro por el segundo parámetro dado
texto_tres = "Naranja"
print(texto_tres.replace("N","T"))

# Uso del operador de pertenencia, verifica si una palabra pertenece una cadena de texto
texto_cuatro = """ Comentarios dedicados a python """
print("dedicados" in texto_cuatro)  # devuelve un true por que existe esta palabra dentro del texto
print("Python" in texto_cuatro)   # devuelve false por que python dentro del texto esta con minúscula
print("u" in texto_cuatro)      # devueve false por que no existe u dentro de esta cadena de texto
