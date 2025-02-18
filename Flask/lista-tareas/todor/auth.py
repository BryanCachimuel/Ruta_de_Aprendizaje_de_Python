from flask import Blueprint, render_template, request, url_for, redirect, flash
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
        
        # buscamos que existen coincidencias entre los nombres de usuarios en la base de datos con el nombre que se va a ingresar por el formulario
        user_name = User.query.filter_by(username = username).first()
        # si el nombre no existe se procede a agregar a la base de datos el nuevo registro
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@bp.route('/login')
def login():
    return render_template('auth/login.html')