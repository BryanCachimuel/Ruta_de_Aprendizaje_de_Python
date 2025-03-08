from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, Flask'

@app.route('/create-article')
def create_article():
    return 'Aqui podemos crear un artículo'

@app.route('/article/<int:article_id>')
def view_article(article_id):
    return f'Estas viendo el artículo número {article_id}'

if __name__ == '__main':
    app.run(debug=True)