from todor import db

# el nombre de esta clase representa a la tabla en la base de datos pero con minuscula user
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
    
# el nombre de esta clase representa a la tabla en la base de datos
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key  = True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)  # agregando una relación de uno a muchos entre las tablas user y todo
    title = db.Column(db.String(100), nullable =  False)
    description = db.Column(db.Text)
    state = db.Column(db.Boolean, default = False)

    # creando un constructor
    def __init__(self, created_by, title, description, state = False):
        self.created_by = created_by
        self.title = title
        self.description = description
        self.state = state

    def __repr__(self):
        return f'<Todo: {self.title}>'