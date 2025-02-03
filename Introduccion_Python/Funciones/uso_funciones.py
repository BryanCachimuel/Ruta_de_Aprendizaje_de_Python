"""
Definición y uso de funciones
"""

def saludar():
    print("Hola desde la función saludar")

saludar()

def saludar(nombre, carrera):
    print(f"Hola {nombre}, bienvenido a la carrera {carrera}")

saludar("Bryan","CISIC")

# funciones con retorno, para este caso para imprimir el resultado
# se debe guardar primero en una variable y luego se manda a imprimir
def saludar(nombre):
    return f"Hola, {nombre} como estas"

# guardando en varaible la función
saludo = saludar("Lennin")

# impresión
print(saludo)

# función que realiza la suma de dos números
def sumar(numero1, numero2):
    suma = int(numero1) + int(numero2)
    return f"El resultado es: {suma}"

resultado = sumar(25,80)

print(resultado)
