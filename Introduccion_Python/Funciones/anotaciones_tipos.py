"""
Anotaciones de Tipos
"""

# se le puede poner el tipo de dato como para que se vea más informativo
# pero no sería muy necesario
a: int = 600
print(a)

# se puede asignar otro valor a la variable a y no pasaría nada
a = "carro"
print(a)

# para estos casos si es necesario poner el tipo de dato para que sea más legible
# -> int esta parte indica el tipo de dato que va a devolver la función
def sumar(a:int, b:int)-> int:
    return a + b

s = sumar(40,55)
print(s)

# también se puede aplicar las anotaciones de la siguiente forma
# si no quiero definir este dato como argumento se lo puede dar un valor
# directamente en el parámetro de la función
def saludo(nombre:str, veces:int=4)->str:
    return f"{nombre}" * veces

sl = saludo("BL")
print(sl)

sl = saludo("BL",10)
print(sl)