from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

app = FastAPI()

# Modelo de datos
# Para decir que un atributo es opcional se debe utilizar la librería Optional
# Este Modelo servirá para registrar datos o para consultar datos

class Movie(BaseModel):
      #id: Optional[int] = None
      id: int
      title: str
      overview: str
      year: int
      rating: float
      category: str

# Modelo para el método update
class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str

# Validación de datos, se usa Field para validar y se pode de dos maneras el defaul en cada atributo del Modelo
class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15, default='My Movie')
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    # para no poner el defaul dentro de los Field
    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'title': 'My Movie',
                'overview': 'Está película trata acerca de ....',
                'year': 2023,
                'rating': 5.2,
                'category': 'Acción'
            }
        }
    }



# para cambiar el puerto por defecto de la aplicación: uvicorn main:app --port 5000
# para que se guarden los cambios en el código sin tener que pausar el servidor: uvicorn main:app --port 5000 --reload
# para hacer que la aplicación  funcione en otros dispositivos que esten conetados a la misma red: 

# Otra forma de acceder a la documentación de la app: http://127.0.0.1:5000/redoc
# configuraciones para mejorar la documentación: para acceder a la misma se pone : http://127.0.0.1:5000/docs
# app.title = "Mi primera aplicación con FastAPI"
# app.version = "0.0.2"


# en la sección tags se agrega este nombre para quitar el nombre default establecido en la documentación
@app.get('/', tags=['Home'])
def home():
    return "Hola desde FastApi"

# Formas de uso del método get y sus tipos de respuesta en el retorno que se puede tener

movies: List[Movie] = []

# se puede enviar una respuesta HTML hacia el cliente
@app.get('/show', tags=['Movies'])
def home():
    return HTMLResponse('<h1>Show The Batman</h1>')


# Obtener el listado de peliculas, -> List[Movie] identifica que está ruta va retornar una lista y de igual forma se muestra en las demás rutas
@app.get('/movies', tags=['Movies'])
def get_movies() -> List[Movie]:
    # return {"movie": "Los Vengadores"}
    return [movie.model_dump() for movie in movies]


# Parámetro en las rutas se agrega en la ruta, en el primer parámetro de la siguiente forma /{id}
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie.model_dump()
    return []

# Parámetros query, su estructura en la url se identifica así: localhost:5000/movies/?id=123
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie.model_dump()
    return []


# Método POST, se agrega el Body para obtener estos resultados desde un formulario
# model_dum nos trae el esquema de los atributos de la clase Movie
@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    # movies.append(movie.model_dump())
    movies.append(movie)
    return [movie.model_dump() for movie in movies]

# Método PUT
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for mv in movies:
        if mv['id'] == id:
            mv['title'] = movie.title
            mv['overview'] = movie.overview
            mv['year'] = movie.year
            mv['rating'] = movie.rating
            mv['category'] = movie.category
    return [movie.model_dump() for movie in movies]
    
# Método delete
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return [movie.model_dump() for movie in movies]