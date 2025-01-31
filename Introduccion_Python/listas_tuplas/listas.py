"""
Listas
"""

colores = ["amarillo","azul","rojo","verde","blanco"]

# recuperar un elemento mediante el indice
print(colores[1])

# recuperar el último elemento mediante el indice
print(colores[-1])

# recuperar la longitud de la lista
print(len(colores))

# agregar un nuevo elemento al final de la lista
colores.append("tomate")
print(colores)

# quitar un elemento
colores.remove("rojo")
print(colores)

# modificar cualquier elemento de la lista
colores[1] = "violeta"
print(colores)

# modificar el ultimo elemento de la lista
colores[-1] = "negro"
print(colores)

# buscar elementos dentro de la lista
print("blanco" in colores)