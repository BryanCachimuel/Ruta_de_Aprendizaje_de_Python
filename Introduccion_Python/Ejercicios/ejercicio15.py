nombre = input("Ingrese su nombre: ")
nombre = nombre.upper()
sexo = input("Ingrese la inicial de su sexo, siendo F femenino y M masculino: ")
sexo = sexo.upper()

if sexo == "F" or sexo == "M":
    if sexo == "M" and nombre[0] > "N":
        print("Pertenece al grupo A")
    elif sexo == "F" and nombre[0] < "M":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
else:
    print("El sexo escogido no es correcto")

