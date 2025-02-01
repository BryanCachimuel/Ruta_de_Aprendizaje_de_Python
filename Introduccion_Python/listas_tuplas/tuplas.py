"""
Tuplas
"""
tupla_1 = (123, 'Lennin',80.5, True)
print(tupla_1)

# Extraer un elemento de la tupla
print(tupla_1[2])

# consultar si existe un elemento en la tupla
print('Lennin' in tupla_1)

# empaquetando y desempaquentado de tuplas
curso = 'Python'
nota = 9
estudiante = 'BLCL'
carrera = 'Sistemas'

# se transforma en una tupla
aprendizaje = curso, nota, estudiante, carrera

print(aprendizaje, type(aprendizaje))

print("La cantidad de elementos de la tupla aprendizaje es de: ", len(aprendizaje))

# forma de desempaquetar una tupla
materia, calificacion, joven, especialidad = aprendizaje

print(materia, calificacion, joven, especialidad, sep = '\n')

# las tuplas a ser inmutables no permiten que se editen, ingresen o eliminen elementos
tupla_1[0] = "Python"

