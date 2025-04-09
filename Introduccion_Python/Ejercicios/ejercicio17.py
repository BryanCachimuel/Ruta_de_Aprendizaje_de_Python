puntuacion = float(input("Ingresa tu puntuación: "))

if puntuacion <= 0.3:
    print("Nivel Inaceptable")
    print("Tu8 dinero conseguido es 0")
elif puntuacion <= 0.5:
    print("Tu nivel es Aceptable")
    print(f"Tu dinero es {2400*puntuacion}")
else:
    print("Tu nivel es Meritorio")
    print(f"Tu dinero es {2400*puntuacion}")