peso = float(input('Ingrese su peso en Kg => '))
estatura = float(input('Ingrese su altura en metros => '))

imc = (peso/(estatura)**2)

imc = round(imc, 2)

print(f'Tú indice de masa corporal es {imc} donde {imc}es el indice de masa corporal')