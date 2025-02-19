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

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo

@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required
def update(id):
    todo = get_todo(id)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html', todo = todo)

# función para eliminar una tarea
@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))