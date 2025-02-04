class Animal:
    """Clase para representar un Animal."""
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad  

    def __str__(self):
        return f"Animal[Especie: {self.especie}, edad: {self.edad}]"



class Mascota(Animal):
    """Clase para representar una mascota, hereda de la clase Animal."""
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.nombre = nombre

    def __str__(self):
        return f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, edad: {self.edad}]"

class RegistroMascotas:
    """Clase para representar un registro de mascotas."""
    def __init__(self):
        self.mascotas = []
