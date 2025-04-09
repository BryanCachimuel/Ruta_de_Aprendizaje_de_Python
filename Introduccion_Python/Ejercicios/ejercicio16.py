renta = int(input("Ingresa la renta: "))

if renta < 10000:
    print("Tipo impositivo de 5%")
elif renta >= 10000 and renta <= 20000:
    print("Tipo impositivo de 15%")
elif renta >= 20000 and renta < 35000:
    print("Tipo impositivo de 20%")
elif renta >= 35000 and renta < 60000:
    print("Tipo impositivo de 30%")
else:
    print("Tipo impositivo de 45%")