"""
Crea un juego de Adivina el número

1) Genera un número aleatorio entre 1 y 100
2) El usuario debe ingresar un número con un limite de 10 intentos
3) Debe ayudar al usuario en cada intento
4) Muestra el resultado de si ganaste o perdiste
"""

import random

print("Bienvenido al Juego de Adivina el Número")

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos_maximos = 10
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos_realizados += 1

    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
        break
    elif intento < numero_secreto:
        print(f"El número es mayor. \nTe quedan {intentos_maximos - intentos_realizados} intentos.")
    else:
        print(f"El número es menor. \nTe quedan {intentos_maximos - intentos_realizados} intentos.")

if intentos_realizados == intentos_maximos:
    print("Perdiste el Juego")