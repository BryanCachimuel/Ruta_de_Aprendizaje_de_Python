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

# para que los errores se puedan ver en el navegador se pone en formato debug cuando se manda a ejecutar el proyecto
# flask --app hello --debug run 