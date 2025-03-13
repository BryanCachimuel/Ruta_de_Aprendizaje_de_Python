from flask import Flask, request, jsonify, session
from models import db
from models.article import Article
from models.user import User
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True)

# configuración de sesiones
app.secret_key = 'python123'

# configuración de sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articulos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Ruta inicial
@app.route('/')
def home():
    return 'Hola, Flask'

# endpoinst para user

# registro de un usuario
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if User.query.filter_by(email = data['email']).first()  is not None:
        return jsonify({
            'error':'El email ya está registrado'
        }), 400

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'message': f'Usuario: {new_user.username} registrado con exito'
    }), 201

# Inicio de sesión de un Usuario
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
   
    if user and user.check_password(data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'message': 'Credenciales invalidas'}), 401

# ruta para verificar si un usuario está autenticado
@app.route('/check-auth', methods=['GET'])
def check_auth():
    if 'user_id' in session:
        return jsonify({'authenticated': True}), 200
    else:
        return jsonify({'authenticated': False}), 401
    
@app.route('/logout', methods=['POST'])
def logout_user():
    session.pop('user_id', None)
    return jsonify({'message':'Sesión cerrada con éxito'})

# Obtener todos los artículos
@app.route('/articles', methods=['GET'])
def list_articles():
    articles = Article.query.all()
    # retornamos en formato json
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'image_url': article.image_url
    } for article in articles ])
    
# Crear un artículo
@app.route('/article', methods=['POST'])
def create_article():
    data = request.get_json()
    new_article = Article(
        title=data['title'], 
        content=data['content'],
        image_url=data['image_url']
        )
    db.session.add(new_article)
    db.session.commit()

    return jsonify({
        'id': new_article.id,
        'title': new_article.title,
        'content': new_article.content,
        'image_url': new_article.image_url
    }), 201

# Actualizar un artículo
@app.route('/articles/<int:id>', methods=['PUT','PATCH'])
def update_article(id):
    article = Article.query.get_or_404(id)
    data = request.get_json()
    article.title = data['title']
    article.content = data['content']
    db.session.commit()

    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content
    })

# Eliminar un artículo
@app.route('/articles/<int:id>', methods=['DELETE'])
def  delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({
        'message':f'Articulo eliminado con exito. Se elimino {article.title}'
    }), 200
       
#Obtener un artículo por id
@app.route('/article/<int:article_id>', methods=['GET'])
def view_article(article_id):
    article = Article.query.get_or_404(article_id)

    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'image_url': article.image_url
    })

if __name__ == '__main':
    app.run(debug=True)