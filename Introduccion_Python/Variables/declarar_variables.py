# Declaración de variables

mensaje = "Hola desde Python"
print(mensaje)

# en python se puede cambiar el valor de una variable y estas variables son conocidas como variables dinámicas
mensaje = "Hola como segundo mensaje"
print(mensaje)

# las variables pueden ser declaradas así en Python
mensaje_nuevo = "Hola este es un segundo mensaje"
print(mensaje_nuevo)

#############################################################################################################

# Números
numero = 20
print(numero)

numero_dos = "30"  # esto es un string

# se imprime 4 veces el valor que se declara en variable_dos
print(numero_dos * 4)

# ver el tipo de dato de una variable
print(type(numero))
print(type(numero_dos))

# declarar números grandes se debe poner guión bajo para que sea más claro o se puede poner el número de forma normal
numero_tres = 1_000_000
print(numero_tres)

# números decimales
numero_cuatro = 18.5
print(numero_cuatro )
print(type(numero_cuatro))

# números grandes en forma de notación científica
numero_cinco = 1e6
print(numero_cinco)

# para conocer el número máximo y mínimo en los números flotantes se usa
import sys
numero_max_float = sys.float_info.max
print(numero_max_float) 

numero_min_float = sys.float_info.min
print(numero_min_float)

# forma de trabajar con números complejos
numeros_complejos = 1 + 5j
print(numeros_complejos)
print(type(numeros_complejos))

# Obteniendo el número real de un número complejo
print(numeros_complejos.real)

# Obteniendo el número imaginario de un número complejo
print(numeros_complejos.imag)