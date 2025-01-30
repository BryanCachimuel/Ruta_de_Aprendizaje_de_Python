"""
Operadores Lógicos
"""

a = 5
b = 7
c = 10

# las dos condiciones deben ser verdaderas para que la respuesta sea verdadera
respuesta_uno = a < b and b < c
print(respuesta_uno)

# si una respuesta es falsa el resultado sera falso
respuesta_dos = a > b and b < c 
print(respuesta_dos)

# vasta con que uno sea cierto para que la respuesta sea verdadera
respuesta_tres = a < b or b < c
print(respuesta_tres)

# si las dos operaciones son falsas el resultado sera falso
respuesta_cuatro = a > b or b > c
print(respuesta_cuatro)

# operador de nagación cambia el valor ya sea true a false y vicerversa
respuesta_cinco = (a > b) or not(b > c)
print(respuesta_cinco)

respuesta_seis = ((a + b) *c > c ** 2) and (c < b)
print(respuesta_seis)

respuesta_siete = ((a + b) *c > c ** 2) or (c < b)
print(respuesta_siete)
