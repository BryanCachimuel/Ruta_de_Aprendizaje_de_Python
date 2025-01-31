"""
Estructura de una cadena
"""
 # len devuelve la cantidad de caracteres tiene una varaible
texto = "Python"
print('Python tiene ', len(texto), ' caracteres.')

# obteniendo el indice de una cadena, tener encuenta que los indices inician desde 0
print('El indice 3 pertenece a la letra: ', texto[3])
print('El indice 5 pertenece a la letra: ', texto[5])

# Para obtener los caracteres desde el lado derecho hacia el izquierdo de un texto se
# debe utilizar números negativos
print('El último caracter del texto es: ', texto[-2])
print('El último caracter del texto es: ', texto[-4])

# Para obtener un trozo del texto se debe utilizar lo siguiente
texto_dos = 'Lenguaje de Programación Python'
print(texto_dos[0:6])
print(texto_dos[12:18])

# desde el inicio asta donde se defina
print(texto_dos[:9])

# para no excluir la última letra del texto se debe poner
print(texto_dos[-3:])

# por que si ponemos así se excluye la última letra y no se toma en cuenta la n
print(texto_dos[-6:-1])

# Para obtener un trozo de texto pero cada dos caracteres desde el inicio del texto
print(texto_dos[::2])

# Para obtener desde el último caracter asta el principio (se obtendra el texto al revez)
print(texto_dos[::-1])

# Para obtener cada dos caracteres desde el final del texto
print(texto_dos[::-2])

# print(texto_dos[:3:2])

# Para simular que sustituimos el valor de un indice dentro de una cadena de texto
texto_tres = "Lennin"
nuevo_texto = "B" + texto_tres[1:] # se excluye el primer indice del texto_tres
print(nuevo_texto)
