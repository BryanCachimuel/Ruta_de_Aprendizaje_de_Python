"""
    Sistema de Descuento en un restaurante 
    Crea un programa en python que simule un sistema de descuentos en un restaurante según el monto 
    de consumo. El programa debe seguir las siguientes instrucciones:
    - Solicita al usuario que ingrese el monto de consumo en el restaurante.
    - Aplica descuentos segun las siguientes reglas:
        1 ) Si el monto de consumo es mayor a $50 pero igual o menor a $100, aplica un descuento del 10%.
        2 ) Si el monto de consumo es mayor a $100 pero igual o menor a $200, aplica un descuento del 20%.
        3 ) Si el monto de consumo es mayor a $200, aplica un descuento del 30%.
        4 ) Si el monto de consumo es igual o menor a $50, no aplica ningún descuento.
    
    Muestra al usuario un resumen de la cuenta con el monto de consumo, el descuento aplicado y el monto 
    final con descuento. 
"""

monto_consumo = float(input('Ingrese el monto del consumo a pagar: '))

if monto_consumo > 50 and monto_consumo <= 100:
    descuento = (monto_consumo * 10)/100
    monto_final = monto_consumo - descuento
    print('Monto de consumo: ', monto_consumo)
    print('Descuento del 10%: ', descuento)
    print('Monto Final: ', monto_final)
elif monto_consumo > 100 and monto_consumo <= 200:
    descuento = (monto_consumo *20)/100
    monto_final = monto_consumo - descuento
    print('Monto de consumo: ', monto_consumo)
    print('Descuento del 20%: ', descuento)
    print('Monto Final: ', monto_final)
elif monto_consumo > 200:
    descuento = (monto_consumo * 30)/100
    monto_final = monto_consumo - descuento
    print('Monto de consumo: ', monto_consumo)
    print('Descuento del 30%: ', descuento)
    print('Monto Final: ', monto_final)
elif monto_consumo <= 50 and monto_consumo >= 0.01:
    descuento = 0
    monto_final = monto_consumo - descuento
    print('Monto de consumo: ', monto_consumo)
    print('Descuento del 0%: ', descuento)
    print('Monto Final: ', monto_final)
else:
    print('Ingrese un monto correcto')