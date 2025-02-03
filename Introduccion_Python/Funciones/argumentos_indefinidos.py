"""
Argumentos Indefinidos
"""

# *args -> definen que podemos poner la cantidad de argumentos que se desee
def args_func(*args):
    print(args)

# devuelve una tupla con todos estos argumentos
args_func("Saludos",550, False, 19.25)

# especificando los valores que le queremos dar a los argumentos
def resta(a, b):
    print(f"a = {a} y b = {b}")
    return a - b

respuesta = resta(500, 100)
print(respuesta)

resuelto = resta(b = 360, a = 555)
print(resuelto)

# argumentos indefinidos con claves y con valores
def kwargs_func(**kwargs):
    print(kwargs)

# me imprime un diccionario
kwargs_func(nombre = "Lennin", a = 250, b = 1800, x = False)

# funciones con argumentos indefinidos y argumentos indefinidos con clave y valor
def argumentos(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

# imprime el primer dato de forma normal el segundo imprime una tupla y el tercero un diccionario
argumentos(500, "Hola", True, 458, nombre="BLCL",b=800)