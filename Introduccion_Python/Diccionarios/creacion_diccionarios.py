"""
Creación y Acceso a Diccionarios
"""

mi_diccionario = {}
print(type(mi_diccionario))

datos_personales = {
    "nombre":"Lennin",
    "edad":30,
    "ciudad":"Ibarra"
}

# para acceder a cada elemento usaremos la clave
print(datos_personales["nombre"])

# para verificar si existe o no una clave
print("edad" in datos_personales)

# método propio de los diccionarios para verificar si existe una clave
# en el caso de no ser encontrada se puede mandar un mensaje
print(datos_personales.get("profesion", "No se especifica"))

# pero si existe la clave nos regresa el valor correspondiente de la clave buscada
print(datos_personales.get("ciudad", "No se especifica"))