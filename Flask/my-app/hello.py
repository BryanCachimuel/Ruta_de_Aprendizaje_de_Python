from flask import Flask

# cuando se pone __name__ estanis diciendo que está es nuestra aplicación de flask
app = Flask(__name__)

# se crean las rutas
# se puede agregar varias rutas a una vista
@app.route('/')
@app.route('/index')
def index():
    return '<h1>Página de Inicio</h1>'

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


# para que los errores se puedan ver en el navegador se pone en formato debug cuando se manda a ejecutar el proyecto
# flask --app hello --debug run 