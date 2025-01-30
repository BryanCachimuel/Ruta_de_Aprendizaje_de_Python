"""
Condicionales
"""

valor_a = 1994
valor_b = 1997

if valor_a > valor_b:
    print('El valor a es mayor al valor b')
else:
    print('El valor b es mayor al valor a')

# Ejercicio par o impar
valor_c = int(input('Ingrese un número: '))

if valor_c % 2 == 0:
    print('El valor c: ', valor_c, ' es par')
else:
    print('El valor c: ', valor_c, ' es impar')


"""
Condicionales anidadas
"""

valor_d = int(input('Ingrese un número: '))

valor_salida = "Es par" if valor_d % 2 == 0 else "Es impar"
print(valor_salida)

# Ejercicio impar o par positivo o negativo

valor_e = int(input('Ingrese un número: '))

if valor_e > 0:
    print("Es par positivo" if valor_e % 2 == 0 else "Es impar positivo")
elif valor_e < 0:
    print("Es par negativo" if valor_e % 2 == 0 else "Es impar negativo")
else:
    print("Es número es cero")