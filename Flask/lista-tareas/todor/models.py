from todor import db

# el nombre de esta clase representa a la tabla en la base de datos
class User(db.Model):
    # creando los atributos de la tabla User
    id = db.Column(db.Integer, primary_key  = True)
    username = db.Column(db.String(20), unique = True, nullable =  False)
    password = db.Column(db.Text, nullable = False)

    # creando un constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # representación de cada usuario para que no se vean como un objeto raro
    # al momento de listar todos los usuarios
    def __repr__(self):
        return f'<User: {self.username}>'