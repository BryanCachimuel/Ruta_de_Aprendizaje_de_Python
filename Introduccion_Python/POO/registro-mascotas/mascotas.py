"""
Programación Orientada a Objetos
"""

# Python recomienda que usemos mayuscula la primera letra en el nombre de una clase

class Animal:

    # atributos de la clase
    especie = ""
    edad = 0

    

# Objeto perro de la clase Animal
perro = Animal()
perro.especie = "Canino"
perro.edad = "1 Año"

gato = Animal()
gato.especie = "Felino"
gato.edad = "6 meses"

print(perro.especie)
print(gato.especie)