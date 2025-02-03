"""
Operaciones Básicas con Diccionarios
"""

datos_personales = {
    "nombre":"Lennin",
    "edad":30,
    "ciudad":"Ibarra",
}

# agregar un nuevo elemento
# pero si no existe la clave se agrega la clave nueva conjunstamente con su valor
datos_personales["genero"] = "masculino"

print(datos_personales)

# si la clave ya existe dentro del diccionario modifica su valor
datos_personales["edad"] = "28"

print(datos_personales)

# otra forma de agregar una clave o valor a diccionario
datos_personales.update({"estudios":"universitarios"})

print(datos_personales)

# otra forma de actualizar un valor de una clave ya existente
datos_personales.update({"estudios":"superiores"})

print(datos_personales)

# con update se puede agregar mas claves y valores respectivos
datos_personales.update({"carrera":"ingenieria","trabajo":"desarrollador","sueldo":600,"certificaciones":"si"})

print(datos_personales)

# eliminar un elemento del diccionario mediante el ingreso del nombre de una de sus claves
del datos_personales["certificaciones"]

print(datos_personales)

# otra forma de eliminar un elemento de diccionario
datos_personales.pop("carrera")

print(datos_personales)

# obtener la logintud de un diccionario
print(len(datos_personales))

# obtener todas claves del direccionario
print(datos_personales.keys())

# obtener una lista de las claves del direccionario
print(list(datos_personales))

# obtener una lista de los valores del direccionario
print(list(datos_personales.values()))

# obtener una lista con las claves y valores del diccionario
print(list(datos_personales.items()))




