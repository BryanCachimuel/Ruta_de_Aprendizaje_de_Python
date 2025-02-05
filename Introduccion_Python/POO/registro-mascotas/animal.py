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

    def agregar_mascota(self, mascota):
        """
        Agrega una mascota al registro

        Parameters:
            mascota (Mascota): La mascota a agregar al registro
        """
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        """
        Lista todas las mascotas registradas
        """
        if self.mascotas:
            print(" Lista de Mascotas \n", "="*30)
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
