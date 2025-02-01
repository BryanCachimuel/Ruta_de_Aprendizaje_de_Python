"""
Bucle while
"""
 # Imprimir los números del 1 al 10

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# Algoritmo de registro de productos
lista_productos = []
producto = ''

while producto.lower() != 'echo':
    producto = input("Ingrese el nombre del producto: (escriba echo para informar que a terminado de agregar productos): ")
    lista_productos.append(producto)

# print(lista_productos)
   
print("\nLista de Productos")
contador = 1
indice = 0

while indice < len(lista_productos):
    print(f"{contador}. {lista_productos[indice]}")
    indice += 1
    contador += 1