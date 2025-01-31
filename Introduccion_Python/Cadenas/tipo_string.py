"""
Uso de Cadenas
"""

# Textos de una sola linea
simple_string = 'Saludos'
doble_string = "Saludos Cordiales estimados"

# Textos con más lineas
texto_grande = '''
                Hola este es un mensaje desde python
                para textos grandes de varias lineas
                como ejemplo
               '''

texto_grandisimo = """
                    Saludos cordiales, estimados estudiantes
                    de la clase de python, estan aprendiendo 
                    un lenguaje sencillo y es bueno que se ponga
                    antención a lo que se va a aprender.
                   """

# Concatenación
texto_uno = 'Hola desarrollador'
texto_dos = 'de python'

texto_concatenado = texto_uno + ' ' + texto_dos

print(texto_concatenado)

# Se puede multiplicar cadenas de texto y estas se erepiten las veces que se defina
print("Hola " * 5) # se repite 5 veces Hola

# Para resaltar un texto dentro de otro se puede usar las comillas simples y las dobles juntas de la siguiente manera
ejemplo_comillas_simple = '"Python" es genial y "exelente"'
print(ejemplo_comillas_simple)

ejemplo_comillas_dobles = "'Python' es un exelente lenguaje de 'programación'"
print(ejemplo_comillas_dobles)

ejemplo_comillas_en_textos_grandes = """
                                     Este es un ejemplo de uso de 'comillas simples'
                                     conjuntamente con las "comillas dobles" y comillas
                                     para textos grandes
                                     """
print(ejemplo_comillas_en_textos_grandes)

# uso de saltos de linea con el caracter especial \n 

ejemplo_comillas_en_textos_grandes_dos = """Ejemplo de uso de 'python' \n en lo que respecta al uso de "cadenas de texto" \n o también llamados 'string'"""
print(ejemplo_comillas_en_textos_grandes_dos)
