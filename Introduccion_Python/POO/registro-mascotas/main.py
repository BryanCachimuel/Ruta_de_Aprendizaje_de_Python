from animal import Mascota, RegistroMascotas

registro = RegistroMascotas()

while True:
    menu = """
            ---------------Menu---------------
            1. Agregar Mascota
            2. Listar Mascotas
            3. Editar Mascota
            4. Eliminar Mascota
            5. Salir
            Ingrese una opción: 
           """
    opcion = input(menu)
    if opcion == "1":
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        edad = input("Edad de la mascota: ")

        mascota = Mascota(especie, edad, nombre)
        registro.agregar_mascota(mascota)

    elif opcion == "2":
        registro.listar_mascotas()