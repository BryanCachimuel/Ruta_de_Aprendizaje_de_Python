from flask import Flask, request, jsonify
from models.article import db, Article

app = Flask(__name__)


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
@app.route('/article', methods=['POST'])
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
        'message':f'Articulo eliminado con exito. Se elimino {article.title}'
    }), 200
       
#Obtener un artículo por id
@app.route('/article/<int:article_id>', methods=['GET'])
def view_article(article_id):
    article = Article.query.get_or_404(article_id)

    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content
    })

if __name__ == '__main':
    app.run(debug=True)