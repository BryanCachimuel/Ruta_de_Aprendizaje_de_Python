"""
Tipos de Errores
"""

# errores de sintaxis (no se puso la commilla final en el print)
# print("Hola desde el terminal)

# error de tipo excpetion (var no esta definida anteriormente y por ende salta el error)
# print(var)

# error de tipo ZeroDivisionError
# div = 4 / 0

# error de tipo (no se pude sumar un string y un entero)
# suma = "4" + 5

# error de tipo value (tranformar un string a entero)
# int("n")

try:
    a = int(input('Ingrese un número entero: '))
    b = int(input('Ingrese un número entero diferente de cero: '))

    resultado = a / b
    
except ValueError:
    print("Error debes ingresar números enteros.") 
except ZeroDivisionError:
    print("Error no se puede dividir entre cero.")
except Exception as e:
    print("Error", e)
else:
    # este else se ejecuta cuando no se han producido niguna de las excepciones
    print(f"División entre {a}/{b} = {resultado}")

