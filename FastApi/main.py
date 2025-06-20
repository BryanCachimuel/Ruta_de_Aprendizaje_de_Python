from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
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
# PlainTextResponse -> imprimir una respuesta sin ningun tipo de formato
@app.get('/', tags=['Home'])
def home():
    return PlainTextResponse(content='Hola desde FastAPI', status_code=200)

# Formas de uso del método get y sus tipos de respuesta en el retorno que se puede tener

movies: List[Movie] = []

# se puede enviar una respuesta HTML hacia el cliente
@app.get('/show', tags=['Movies'])
def home():
    return HTMLResponse('<h1>Show The Batman</h1>')


# Obtener el listado de peliculas, -> List[Movie] identifica que está ruta va retornar una lista y de igual forma se muestra en las demás rutas
# El tercer parámetro del decorador de la función indica el códiogo y descripción de estado de la documentación
# El código de estado del retorno indica el estado de la respuesta
@app.get('/movies', tags=['Movies'], status_code=200, response_description='Nos debe devolver una respuesta exitosa')
def get_movies() -> List[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)


# Parámetro en las rutas se agrega en la ruta, en el primer parámetro de la siguiente forma /{id}
# Validaciones de parámetros
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404)

# Parámetros query, su estructura en la url se identifica así: localhost:5000/movies/?id=123
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return JSONResponse(content=movie.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404)


# Método POST, se agrega el Body para obtener estos resultados desde un formulario
# model_dum nos trae el esquema de los atributos de la clase Movie
# RedirectResponse -> redirige hacia una ruta y se agrega el estado del código
@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=201)
    #return RedirectResponse('/movies', status_code=303)
    

# Método PUT
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for mv in movies:
        if mv.id == id:
            mv.title = movie.title
            mv.overview = movie.overview
            mv.year = movie.year
            mv.rating = movie.rating
            mv.category = movie.category
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)
    
# Método delete
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)


# Probando el tipo de respuesta de archivo
@app.get('/get_file')
def get_file():
    return FileResponse('file.pdf')