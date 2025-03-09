from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# configuración de sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articulos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# Modelo de Artículo
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # se imprime por consola el titulo del artículo
    def __repr__(self):
        return f'<Article: {self.title}>'

with app.app_context():
    db.create_all()

# Ruta inicial
@app.route('/')
def home():
    return 'Hola, Flask'

# Obtener todos los artículos
@app.route('/articles', methods=['GET'])
def list_articles():
    articles = Article.query.all()
    # retornamos en formato json
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'content': article.content
    } for article in articles ])
    
# Crear un artículo
@app.route('/create-article', methods=['POST'])
def create_article():
    data = request.get_json()
    new_article = Article(title=data['title'], content=data['content'])
    db.session.add(new_article)
    db.session.commit()

    return jsonify({
        'id': new_article.id,
        'title': new_article.title,
        'content': new_article.content
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
        'message':f'Articulo {id} eliminado con exito'
    }), 200
       
#Obtener un artículo por id
@app.route('/article/<int:article_id>')
def view_article(article_id):
    article = Article.query.get_or_404(article_id)

    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content
    })

if __name__ == '__main':
    app.run(debug=True)