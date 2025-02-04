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
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad  

    # self indica que esté es un método de la clase Animal
    def __str__(self):
        return f"Animal[Especie: {self.especie}, edad: {self.edad}]"

"""
animal1 = Animal("Perro","1 año")
animal2 = Animal("Gato","6 meses")

print(animal1.especie)
print(animal2.especie)

animal1.informacion()
animal2.informacion()
"""

# entre parentesis se coloca de que clase se quiere heredad
class Mascota(Animal):
    # al heredar de la clase Animal se debe poner todos los atributos de instancia y agregar
    # en la parte inferior super seguido de los atributos de instancia
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.nombre = nombre

    # se puede modificar el método de la clase Animal para poder imprimir los atributos de 
    # instancia propios de la clase Mascota
    def informacion(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, edad: {self.edad}")
    
    def hablar(self):
        pass
    
    def __str__(self):
        return f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, edad: {self.edad}]"

# mascota = Mascota("Perro","2 años","Bobby")
# mascota.informacion()
# print(mascota.__str__())

class Perro(Mascota):
    def hablar(self):
        return "Woof!"

class Gato(Mascota):
    def hablar(self):
        return "Miau!"
    
p = Perro("Canino","1 Año", "Boddy")
g = Gato("Felino","2 Años", "Pelusa")

print(p.hablar())
print(g.hablar())