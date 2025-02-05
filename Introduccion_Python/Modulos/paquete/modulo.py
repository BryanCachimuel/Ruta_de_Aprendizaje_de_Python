"""
Paquetes
"""

def aviso():
    print("Aviso desde el módulo")

from paquete import variable_global

print(variable_global)

print("__name__ en modulo.py", __name__)

if __name__ == "__main__":
    print("Esto se ejecuta solo cuando el modulo.py se ejecuta con el programa principal")