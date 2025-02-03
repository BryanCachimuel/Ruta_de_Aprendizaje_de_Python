"""
Sistema de registro de estudiantes
El sistema debe permitir
1) Registro de Estudiantes:
    1.1) Capturar información del estudiante desde la terminal, incluyendo nombre, edad, curso
    1.2) Almacenar la información en un diccionario
2) Almacenamiento en una lista:
    2.1) Guardar cada diccionario de estudiante en una lista centrar
3) Visualización del registro:
    3.1) Mostrar el registro completo de estudiantes, incluyendo sus detalles como: nombre,edad y curso
"""

registro_estudiantes = []

# creando un menu de navegación
while True:
    print("1. Registrar Estudiante")
    print("2. Mostrar Registro")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        # Registrar estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        curso = input("Ingrese el curso del estudiante: ")

        # creando un diccionario para cada estudiante
        estudiante = {"Nombre":nombre, "Edad":edad, "Curso":curso}
        registro_estudiantes.append(estudiante)
        print("Estudiante registrado exitosamente!\n")

    elif opcion == '2':
        if registro_estudiantes:
            print("\nRegistro de Estudiantes: ")
            for estudiante in registro_estudiantes:
                print(f"Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso: {estudiante["Curso"]} \n")
        else:
            print("El Registro está vacío. Registre primero un estudiante.\n")
    
    elif opcion == '3':
        print("Saliendo del programa. Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")