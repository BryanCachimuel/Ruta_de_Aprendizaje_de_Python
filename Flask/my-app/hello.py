from flask import Flask

# cuando se pone __name__ estanis diciendo que está es nuestra aplicación de flask
app = Flask(__name__)

# se crea una ruta
@app.route('/')
def saludo():
    return 'Saludos desde Flask'

# para que los errores se puedan ver en el navegador se pone en formato debug cuando se manda a ejecutar el proyecto
# flask --app hello --debug run 