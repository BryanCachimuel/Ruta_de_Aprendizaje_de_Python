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


    def editar_mascota(self, indice, nueva_mascota):
        """
        Edita una mascota en el registro.

        Parameters:
            indice (int): El  indice de la mascota a editar
            nueva_mascota (Mascota): La nueva información de la mascota
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            self.mascotas[indice] = nueva_mascota
            print("Mascota editada correctamente.")


    def eliminar_mascota(self, indice):
        """
        Elimina una mascota en el registro.

        Paramters:
            indice (int): El  indice de la mascota a eliminar   
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            del self.mascotas[indice]
            print("Mascota eliminada correctamente.")
