"""
Entrada de datos
"""
ingreso_mensaje = input('Ingrese un mensaje: ')
print(ingreso_mensaje)

"""
Conversión de tipos de datos, con comentarios de bloques
"""
numero_uno = input('Ingrese el primer número: ')
numero_dos = input('Ingrese el segundo número: ')

# conversión de string a entero
numero_uno = int(numero_uno)
numero_dos = int(numero_dos)

suma = numero_uno + numero_dos

print('La suma es: ' , suma)

# conversión de entero a string
numero_tres = 15;
numero_tres = str(numero_tres)
print('El nnúmero: ', numero_tres, 'Es de un tipo de dato: ', type(numero_tres)) 