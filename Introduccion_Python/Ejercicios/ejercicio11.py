contrasenia = 'ctrlblcl'

ingresar_contrasenia = input('Ingrese una constraseña: ')

ingresar_contrasenia = ingresar_contrasenia.lower()

if contrasenia == ingresar_contrasenia:
    print('Las contraseñas son iguales')
else:
    print('Las contraseñas no son iguales')