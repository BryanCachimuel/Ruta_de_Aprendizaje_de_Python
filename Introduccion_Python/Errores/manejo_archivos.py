"""
Manejo de Archivos
"""
try:
    # se abre el archivo para leerlo
    with open("archivo.txt","r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
    print("Creando el archivo...")
    with open("archivo.txt","w") as archivo:
        archivo.write("Creando un archivo para trabajar con python")
else:
    print("Contenido del archivo: ")
    print(contenido)

