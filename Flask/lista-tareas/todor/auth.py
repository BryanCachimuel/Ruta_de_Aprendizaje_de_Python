from flask import (
                    Blueprint, 
                    render_template, 
                    request, 
                    url_for, 
                    redirect, 
                    flash,
                    session,
                    g
                   )
from werkzeug.security import generate_password_hash, check_password_hash

# importando la base de datos
from .models import User

from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, generate_password_hash(password))

        error = None
        
        # buscamos que existen coincidencias entre los nombres de usuarios en la base de datos con el nombre que se va a ingresar por el formulario
        user_name = User.query.filter_by(username = username).first()
        # si el nombre no existe se procede a agregar a la base de datos el nuevo registro
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya está registrado'
        
        # proceso para mostrar un mensaje de error en la vista
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        
        # validar datos
        user = User.query.filter_by(username = username).first()
        
        if user == None:
            error = 'Nombre de Usuario Incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña Incorrecta'
        
        # Iniciar Sesión
        # si no existe un error
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))
        
        # proceso para mostrar un mensaje de error en la vista
        flash(error)
    return render_template('auth/login.html')

# Mantener la sesión iniciada
# con este decorador se dice que esta registrando está función se ejecute en cada petición
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)