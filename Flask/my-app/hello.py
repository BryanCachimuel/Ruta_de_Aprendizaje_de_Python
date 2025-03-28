from flask import Flask, render_template, url_for, request
from datetime import datetime

# cuando se pone __name__ estanis diciendo que está es nuestra aplicación de flask
app = Flask(__name__)

# cuando se trabaja con formularios o sesiones se debe agregar una clave secreta
app.config.from_mapping(
    SECRET_KEY = 'dev'
)

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


# Crear formulario con wtform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre de Usuario: ", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField("Registrar")

# Registrar Usuario
# definimos que vamos a usar dos tipos de métodos
# GET -> para renderizar a la vista regiter
# POST -> para procesar los datos que se envien por el formulario
# importamos request para capturar las información del cliente que envié por el formulario
@app.route('/auth/register', methods = ['GET','POST'])
def register():
    # instancia de la clase RegisterForm
    form = RegisterForm()
    # se capturan los datos
    if request.method == 'POST': 
       

        # valida los datos que se ingresen y también valida los datos en el método POST
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            return f"Nombre de usuario: {username}, Contraseña: {password}"

        '''
            username = request.form['username']
            password = request.form['password']
        if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
            return f"Nombre de usuario: {username}, Contraseña: {password}"
        else: 
            error = """Nombre de usuario debe tener entre 4 a 25 caracteres y
            la contraseña debe tener entre 6 a 40 caracteres
            """
            return render_template('auth/register.html', form = form, error = error)
        '''

    return render_template('auth/register.html', form = form)

# para que los errores se puedan ver en el navegador se pone en formato debug cuando se manda a ejecutar el proyecto
# flask --app hello --debug run 