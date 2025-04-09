edad = int(input("Ingresa tu edad: "))

if edad < 4:
    print("Es gratis")
elif edad >= 4 and edad < 18:
    print("Tienes que pagar $5")
else:
    print("Tienes que pagar $10")