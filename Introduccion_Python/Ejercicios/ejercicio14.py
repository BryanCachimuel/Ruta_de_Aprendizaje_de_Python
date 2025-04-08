edad = int(input('Ingresa tu edad: '))
ingresos = int(input('Coloca tus ingresos: '))

if edad >= 16 and ingresos >= 1000:
    print("Tienes que pagar Impuestos")
else:
    print("No tienes que pagar Impuestos")