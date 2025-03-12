# Modelo de Artículo
from models import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))

    # se imprime por consola el titulo del artículo
    def __repr__(self):
        return f'<Article: {self.title}>'