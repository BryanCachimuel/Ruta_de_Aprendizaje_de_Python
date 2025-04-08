ahorro = int(input('Ingresa tu dinero a ahorrar: '))

primer_anio = round((ahorro * 1.04),2)
segundo_anio = round((primer_anio * 1.04),2)
tercer_anio = round((segundo_anio * 1.04),2)

print(f'El primer año de ahorro es de $ {primer_anio}')
print(f'El segundo año de ahorro es de $ {segundo_anio}')
print(f'El tercer año de ahorro es de $ {tercer_anio}')