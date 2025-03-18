from datetime import datetime
# Modelo de Artículo
from models import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    is_favorite = db.Column(db.Boolean, default=False, nullable=False)

    # se imprime por consola el titulo del artículo
    def __repr__(self):
        return f'<Article: {self.title}>'