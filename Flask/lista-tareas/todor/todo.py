from flask import Blueprint

# Blueprint permite organizar las vistas del proyecto

# con el __name__ estamos mandando la configuración del modulo actual
# url_prefix='todo/' indica la ruta inicial por donde va a iniciar el proyecto
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
def index():
    return "Lista de tareas"

@bp.route('/create')
def create():
    return "Crear una tarea"