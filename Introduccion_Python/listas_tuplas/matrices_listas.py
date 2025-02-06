"""
Matrices con listas anidadas
"""

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# Imprimir la matriz para que se vea una matriz adecuadamente
print(f"{matriz[0]} \n{matriz[1]} \n{matriz[2]}")

# Mostrar el número 1
print(f"Mostrar el número: {matriz[0][0]}")

# Mostrar el número 4
print(f"Mostrar el número: {matriz[1][0]}")

# Mostrar el número 8
print(f"Mostrar el número: {matriz[2][1]}")

# Mostrar el número 3
print(f"Mostrar el número: {matriz[0][2]}")

# recorrido de la matriz mediante el ciclo for
matrix = [[4,8,12],
          [16,20,24],
          [28,32,36]]

print("Mostrar todos los elementos de la matriz fila por fila")
for row in matrix:
    print(row)

print("Mostrar todos los elementos de la matriz elemento a elemento en columna")
for row in matrix:
    for element in row:
        print(element)

print("Mostrar todos los elementos de una matriz en formato de matriz")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()