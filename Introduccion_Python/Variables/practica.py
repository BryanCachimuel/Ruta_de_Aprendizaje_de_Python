"""
Calcular el Precio de Venta

Dado el valor de la venta de un producto, se debe calcular un impuesto del 18% y
apartir de eso, determinar el precio de la venta final

En esta práctica, se va a crear un programa que permita al usuario ingresar el valor
de venta del producto. Luego el sistema realizará los cálculos necesarios para hallar
el impuesto y el precio de venta 

"""
# Solicitar al usuario ingresar los valores correspondientes
producto = input('Ingrese el nombre de un producto: ')
valor_producto = float(input('Ingrese el valor del producto: '))

valor_impuesto = (valor_producto * 18)/100

valor_total = valor_producto + valor_impuesto

print('Valor del impuesto: ', valor_impuesto)
print('Valor de la venta con impuestos: ' , valor_total)