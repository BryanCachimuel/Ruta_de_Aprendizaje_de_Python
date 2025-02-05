"""
Uso de Módulos
"""
# para poder darle un alias al modulo datetime se puede poner as seguido de un nombre cualquiera
import datetime as dt

# se puede decidir que solo vamos a utilizar un método del modulo importado
from datetime import date as d

# para usar todas las funciones de un módulo se pone *
# from datetime import *

# obtiene la fecha de hoy
hoy = d.today()
print(hoy)

# obtiene la fecha y hora actual
hoy = dt.datetime.now()
print(hoy)