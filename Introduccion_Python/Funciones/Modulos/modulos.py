"""
Crear Modulos en Python
"""
import random
from typing import List, Dict

def formato_aleatorio()->str:
    formatos = [
        "¡Hola, {}! ¡Bienvenido!",
        "¡Es genial verte, {}!",
        "¡Saludos, {}! ¡Encantado de conocerte!",
    ]

    return random.choice(formatos)

# print(formato_aleatorio())

def nombre_saludo(nombre:str)->str:
    if nombre == "":
        return "Error: Nombre vació."
    
    saludo = formato_aleatorio().format(nombre)
    return saludo

print(nombre_saludo("Bryan"))

# función que recibira una lista de nombres y retornará un diccionario
def nombres_saludos(nombres:List)->Dict:
    saludos = {}
    for nombre in nombres:
        saludo = nombre_saludo(nombre)
        saludos[nombre] = saludo

    return saludos

# creando una lista con nombres
# nombres = ["Nelson","Cristoper","Kevin","Lucas","Richard"]

# print(nombres_saludos(nombres))