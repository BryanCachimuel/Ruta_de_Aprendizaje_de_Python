from flask import Blueprint, render_template, request, redirect, url_for, g

from todor.auth import login_required

from .models import Todo, User
from todor import db

# Blueprint permite organizar las vistas del proyecto

# con el __name__ estamos mandando la configuración del modulo actual
# url_prefix='todo/' indica la ruta inicial por donde va a iniciar el proyecto
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
@login_required  # decorador que indica que para ingresar a esta vista se necesita iniciar sesión
def index():
    # recuperando todas las tareas
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        todo = Todo(g.user.id, title, description)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')