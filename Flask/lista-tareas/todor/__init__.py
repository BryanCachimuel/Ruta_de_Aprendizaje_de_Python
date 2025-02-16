from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# creando una extensión de SQLAlchemy
db = SQLAlchemy()

# 1. esta función se crea para realizar instancias de la aplicación
# está instancia puede servir cuando se hace una conexión hacia la base de datos
# o cuando se hace una instancia para testear al aplicación
def create_app():
    app = Flask(__name__)

    # 2. Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///listatareas.db"
    )

    # inicializa la conexión hacia la base de datos
    db.init_app(app)

    # registrar Blueprint de todo
    from . import todo
    app.register_blueprint(todo.bp)

   # registrar Blueprint de auth
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    # migra todos los modelos que se van a crear hacia la base de datos
    with app.app_context():
        db.create_all()

    return app