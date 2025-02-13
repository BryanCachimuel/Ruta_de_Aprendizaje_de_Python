from flask import Flask, render_template, url_for, request
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
#@app.route('/index')
def index():
    print(url_for('index'))
    print(url_for('animales'))
    print(url_for('animales', nombre='Jack'))
    print(url_for('animales', nombre='Jack', edad=20))
    print(url_for('code',code='print("Hola")'))
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
@app.route('/mascotas/<nombre>/<int:edad>')
@app.route('/mascotas/<string:nombre>/<int:edad>/<email>')
def animales(nombre = None, edad = None, email = None):
    mis_datos = {
        'nombre': nombre,
        'edad' : edad,
        'email' : email
    }
    return render_template('mascotas.html', datos = mis_datos)

# escape de html -> permite que no se realicen ataques a nuestros sistemas
# ya que mediante la url se puede ingresar scripts y mediante escape estos 
# scripts se muestran como textos en pantalla
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

# Registrar Usuario
# definimos que vamos a usar dos tipos de métodos
# GET -> para renderizar a la vista regiter
# POST -> para procesar los datos que se envien por el formulario
# importamos request para capturar las información del cliente que envié por el formulario
@app.route('/auth/register', methods = ['GET','POST'])
def register():
    # se capturan los datos
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        return f"Nombre de usuario: {username}, Contraseña: {password}"
    return render_template('auth/register.html')

# para que los errores se puedan ver en el navegador se pone en formato debug cuando se manda a ejecutar el proyecto
# flask --app hello --debug run 