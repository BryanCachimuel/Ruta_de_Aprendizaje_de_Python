from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configuración de sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articulos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # se imprime por consola el titulo del artículo
    def __repr__(self):
        return f'<Article: {self.title}>'


@app.route('/')
def home():
    return 'Hola, Flask'

@app.route('/create-article', methods=['GET','POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        return f'Artículo creado: {title}, Contenido: {content}'
    
    return '''
        <form method="POST" action="create-article">
            <label for="title">Título del artículo: </label><br/>
            <input type="text" id="title" name="title"/><br/><br>

            <label for="content">Contenido del artículo:</label><br/>
            <textarea name="content" id="content"></textarea><br/><br>

            <input type="submit" value="Crear Artículo"/>
        </form>
'''

    return 'Aqui podemos crear un artículo'

@app.route('/article/<int:article_id>')
def view_article(article_id):
    return f'Estas viendo el artículo número {article_id}'

if __name__ == '__main':
    app.run(debug=True)