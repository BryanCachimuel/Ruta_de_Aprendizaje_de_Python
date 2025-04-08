pan_pasado = int(input('Ingresa el número de barras de pan pasadas vendidas: '))

total_pan_pasado = round(((pan_pasado * 3.49) * 0.6),2)

fresco_pan_pasado = round((pan_pasado * 3.49),2)

descuento = round((fresco_pan_pasado - total_pan_pasado),2)

print(f"El precio habitual del pan {fresco_pan_pasado}, el descuento que se hizo fue de {descuento} y el coste final es {total_pan_pasado}")

