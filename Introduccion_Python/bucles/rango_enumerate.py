"""
Rango y enumerate
"""

# range -> no incluye el 5
for n in range(5):
    print(n)

print("\n")

# rango desde el 10 al 20 -> sin considerar al 20
for n in range(10,20):
    print(n)

print("\n")

# rando del 20 al 40 pero saltando de 2 en 2
for n in range(20,40,2):
    print(n)

print("\n")

# enumerate -> indica 2 paramétros indice de cada elemento y el valor determina como los nombres dados a cada elemento de la lista
animales = ["perro","gato","conejo","cerdo","oveja","abeja","caballo"]

for indice, valor in enumerate(animales):
    print(indice, valor)

print("\n")

# inicia el conteo del indice en 1 gracias a segundo parámetro de enumerate
for indice, valor in enumerate(animales, start=1):
    print(indice, valor)

