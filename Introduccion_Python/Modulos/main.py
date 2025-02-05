"""
Uso de Módulos
"""
# para poder darle un alias al modulo datetime se puede poner as seguido de un nombre cualquiera
import datetime as dt

# se puede decidir que solo vamos a utilizar un método del modulo importado
from datetime import date as d

# usando paquetes externos
from colorama import init, Fore

# se inicializa el paquete externo
init()

# si estamos en el archivo principal se podrá ejecutar el código que esta más abajo
if __name__ == "__main__":

    # para usar todas las funciones de un módulo se pone *
    # from datetime import *

    # obtiene la fecha de hoy
    hoy = d.today()
    print(hoy)

    # obtiene la fecha y hora actual
    hoy = dt.datetime.now()
    print(hoy)

    # mandamos a llamar al directorio y archivo paquete/modulo
    from paquete.modulo import aviso

    from paquete import modulo

    modulo.aviso()

    # Caso de uso de la palabra reservada __name__ para desiganr un archivo principal
    print(__name__)

    print(Fore.RED + "Este es un mensaje rojo")
    print(Fore.GREEN + "Este es un mensaje verde")
    print(Fore.BLUE + "Este es un mensaje azul")    

    # para instalar un paquete externo se debe utilizar pip install colorama
    # para desinstalar un paquete se debe poner pip uninstall colorama



    # Crear un entorno virtual        -> python -m -venv -env
    # Para activar un entorno virtual -> .env\Scripts\activate
    # Para salir del entorno virtual  -> deactivate
 
