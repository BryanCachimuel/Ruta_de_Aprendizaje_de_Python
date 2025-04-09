import sys

print("Bienvenido...")
print("Ingresa el modo de trabajo")
modo = int(input("[1]. Suma\n[2]. Resta\n[3]. Multiplicación\n[4]. División\n ==>"))

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

if modo == 1:
    suma = numero1 + numero2
    print(f"La suma de los númeroses: {suma}")
elif modo == 2:
    resta = numero1 - numero2
    print(f"La resta de los númeroses: {resta}")
elif modo == 3:
    multilicacion = numero1 * numero2
    print(f"La multiplicación de los númeroses: {multilicacion}")
elif modo == 4:
    if numero2 == 0:
        print("No se puede dividir entre 0")
        sys.exit()
    else:
        division = numero1 / numero2
        print(f"La divisón de los númeroses: {division}")
else:
    print("Modo Ingresado Incorrecto")