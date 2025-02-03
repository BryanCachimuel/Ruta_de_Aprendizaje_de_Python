"""
Crear Modulos en Python
"""
import random

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