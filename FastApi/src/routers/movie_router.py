from fastapi import Path, Query
from fastapi.responses import JSONResponse
from typing import List

movies: List[Movie] = []

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
