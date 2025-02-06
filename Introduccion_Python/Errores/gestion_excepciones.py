"""
Gestión de Excepciones
"""

# crear nuestra propia excepción
class ColorNoValidoError(Exception):
    def __init__(self, color):
        super().__init__(f"El color {color} no se encuentra en la lista")

def colores(color):
    lista_colores = ["azul","verde","rojo"]

    # si el color no está en la lista devolvemos una excepción
    # if color not in lista_colores:
    #     raise Exception(f"El color {color} no se encuentra en la lista")
    # else:
    #   print(f"El color {color} si está en la lista")

    # usando nuestra propia excepción
    if color not in lista_colores:
        raise ColorNoValidoError(color)

try:
    colores("naranja")
except ColorNoValidoError as error:
    print(f"Error: {error}")