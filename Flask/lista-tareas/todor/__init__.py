from flask import Flask, render_template

# 1. esta función se crea para realizar instancias de la aplicación
# está instancia puede servir cuando se hace una conexión hacia la base de datos
# o cuando se hace una instancia para testear al aplicación
def create_app():
    app = Flask(__name__)

    # 2. Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev'
    )

    # registrar Blueprint de todo
    from . import todo
    app.register_blueprint(todo.bp)

   # registrar Blueprint de auth
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app