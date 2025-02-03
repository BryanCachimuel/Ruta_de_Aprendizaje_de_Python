"""
Iteracción sobre diccionarios
"""
datos = {
    "nombre":"Lennin",
    "edad":30,
    "ciudad":"Ibarra"
}
# se obtiene la clave de los diccionarios
for valor in datos:
    print(valor)

# se obtiene los valores de los diccionarios
for valor in datos:
    print(datos[valor])

# otra forma de obtener los valores de los diccionarios
for valor in datos.values():
    print(valor)

# Para obtener claves y valor
for clave, valor in datos.items():
    print(clave, valor)
