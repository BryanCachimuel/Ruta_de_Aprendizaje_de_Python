"""
Mnipulación de Listas
"""

lista1 = [1,2,3]
lista2 = [4,5,6]

# concatenar dos listas
lista3 = lista1 + lista2
print(lista3)

# multiplicar una lista las veces necesarias
print(lista1 * 3)

# obtener una sublista estableciendo que elementos queremos en esa sublista
lista5 = lista3[0:3]
print(lista5)

# obtener una sublista estableciendo que elementos queremos en esa sublista
lista5 = lista3[:-2] # se omiten los ultimos dos elementos de la lista
print(lista5)

lista6 = lista3[-3:] 
print(lista6)

lista7 = lista3[-3:-1] 
print(lista7)

# obtener de 2 en 2 los elemetos
lista8 = lista3[::2]
print(lista8)

# obtener solo valores pares
lista9 = lista3[1::2]
print(lista9)

# invertir la lista
lista10 = lista3[::-1]
print(lista10)

# ordenar los elementos de una lista de forma ascendente
lista11 = [5,3,12,6,15,22,1,4]
lista11.sort()
print(lista11)

# también ordena los elementos de una lista de forma ascendente
print(sorted(lista11))

# ordenar los elementos de una lista de forma descendente
lista11 = [5,3,12,6,15,22,1,4]
lista11.sort(reverse=True)
print(lista11)

# obtener el número mayor de una lista
print(max(lista11))

# obtener el número menor de una lista
print(min(lista11))

# sumar todos los elementos de una lista
print(sum(lista11))



