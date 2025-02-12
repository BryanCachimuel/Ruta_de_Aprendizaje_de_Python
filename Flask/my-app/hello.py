from flask import Flask, render_template
from datetime import datetime

# cuando se pone __name__ estanis diciendo que está es nuestra aplicación de flask
app = Flask(__name__)

# se pueden aplicar fitros personalizados
# para que esto quede registrados en los filtros de flask o Jinja2 se debe aplicar el decorador @app.add_template_filter
# estos filtros se van a poder utilizar en toda la aplicación
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')  # formato en que queremos se presente la fecha

# la función today también se puede registrar de esta manera como un filtro para toda la aplicación
# app.add_template_filter(today, 'today')

# creando una función personalizada
# con el decorador @app.add_template_global permite que está función no se necesaria de enviar como renderizado hacia la vista index.html
#@app.add_template_global
def repeat(cadena, numero):
    return cadena * numero

# o también se puede utilizar lo siguiente para que está función sea global dentro de la aplicación
app.add_template_global(repeat, 'repeat')

# se crean las rutas
# se puede agregar varias rutas a una vista
# con render_template se puede redirigir hacia una vista con html
# se manda como parámetro la variable name hacia la vista
# a una vista se le puede enviar diferentes tipos de datos como: strings, listas


@app.route('/')
@app.route('/index')
def index():
    name = 'Jenny'
    friends = ['Nelson','Cristoper','Kevin','Michelle']
    date = datetime.now()
    return render_template(
                           'index.html', 
                           name = name, 
                           friends = friends, 
                           date =  date
                           #repeat = repeat
                           )

@app.route('/saludo')
def saludo():
    return '<h1>Página de Saludos</h1>'

# se puede poner variables en las rutas mediante el uso de -> <>
@app.route('/asignando/<nombre>')
def asignar(nombre):
    return f'<h1>Página de asignación de nombres. ejemplo: {nombre}</h1>'

# se puede poner el tipo de dato que se manda en las variables de la url
# pueden ser de tipo: string, int, float, path, uuid

@app.route('/datos/<string:nombre>/<int:edad>')
def informacion(nombre,edad):
    return f'<h1>Hola tu información es: nombre: {nombre} y tu edad es: {edad} años</h1>'

# variables en las rutas con condicionales
@app.route('/mascotas')
@app.route('/mascotas/<nombre>')
@app.route('/mascotas/<string:nombre>/<int:edad>')
def animales(nombre = None, edad = None):
    if nombre == None and edad == None:
        return '<h1>Saludos a todos los animales</h1>'
    elif edad == None:
        return f'<h1>Holas, {nombre}</h1>'
    else:
        return f'<h1>Hola mascota de nombre: {nombre}, tu doble de edad es: {edad*2} años</h1>'

# escape de html -> permite que no se realicen ataques a nuestros sistemas
# ya que mediante la url se puede ingresar scripts y mediante escape estos 
# scripts se muestran como textos en pantalla
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

# para que los errores se puedan ver en el navegador se pone en formato debug cuando se manda a ejecutar el proyecto
# flask --app hello --debug run 