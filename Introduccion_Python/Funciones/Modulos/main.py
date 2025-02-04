"""
Importar mi modulo
"""
# forma 1 de importar el modulo 
import modulos

# forma 2 de importar el modulo y manda a importar todas las funciones con el *
from modulos import *

# se manda a importar solo la función nombre saludo y nombres_saludos
from modulos import nombre_saludo, nombres_saludos

print(nombre_saludo("Adriana"))

nombres = ["Angelita","Deysi","Marlene","Silvana"]
saludos = nombres_saludos(nombres)

for saludo in saludos.values():
    print(saludo)

# Nota: al utilizar modulos propios se crea un directorio con un archivo en el cual contiene
# la compilación del proceso con el que se esté trabajando dentro de los modulos
# para este caso se creo un directorio con el nombre _pycache_ con el archivo modulos.crython-313.pyc