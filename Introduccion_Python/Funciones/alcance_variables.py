"""
Alcance de las variables (scope)
"""
# vareiable global
numero_mayor = 25
numero_menor = 15

def dividir():
    resultado = numero_mayor / numero_menor
    print(f"el resultado es: {resultado}")

dividir()

# variables locales solo se usan dentro de la función
def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    print(locals())

# la impresión me da como resultado: {'numero1': 12, 'numero2': 12, 'resultado': 144}
multiplicacion(12,12)

# Para actualizar el valor de una variable global
a = 0

def actualizar():
    global a
    a += 2

actualizar()


# Trabajando con funciones anidadas
def funcion1():
    c = 0
    def funcion2():
        nonlocal c  # se transforma c en una variable no local para poder modificar el valor de c
        c += 1
    funcion2()
    print(c)

funcion1()