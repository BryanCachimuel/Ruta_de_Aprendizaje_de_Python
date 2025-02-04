"""
Programación Orientada a Objetos
"""

# Python recomienda que usemos mayuscula la primera letra en el nombre de una clase

class Animal:

    # atributos de la clase
    # especie = ""
    # edad = 0


    # constructor
    # self hace referencia a la clase
    # especie y edad en este caso son atributos de instancia
    def __init__(self, especie, edad)->None:
        self.especie = especie
        self.edad = edad  

    # self indica que esté es un método de la clase Animal
    def informacion(self):
        print(f"Especie: {self.especie}, edad: {self.edad}")

animal1 = Animal("Perro","1 año")
animal2 = Animal("Gato","6 meses")

print(animal1.especie)
print(animal2.especie)

animal1.informacion()
animal2.informacion()