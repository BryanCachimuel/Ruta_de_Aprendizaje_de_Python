"""
Bucle for
"""

numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    print(numero)

print("\n")

mensaje = "Saludos con Python"

for msj in mensaje:
    print(msj)

# Algoritmo de registro de productos

lista_productos = []
producto = ''

while producto.lower() != 'echo':
    producto = input("Ingrese el nombre del producto: (escriba echo para informar que a terminado de agregar productos): ")
    lista_productos.append(producto)

print("\nLista de Productos")
contador = 1

for producto in lista_productos:
    print(f"{contador}. {producto}")
    contador += 1
