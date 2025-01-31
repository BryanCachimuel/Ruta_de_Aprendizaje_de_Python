"""
Verificar que una palabra sea palíndroma
"""

palabra = input('Ingrese una palabra: ')

# transformando una palabra ingresada a mínusculas
palabra = palabra.lower();

# borrando los espacios en una palabra
palabra = palabra.replace(" ","")

# invertimos la palabra
palabra_invertida = palabra[::-1]

# verificar si la palabra es palindroma
if palabra == palabra_invertida:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")
