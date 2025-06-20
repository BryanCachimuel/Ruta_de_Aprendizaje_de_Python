from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, field_validator
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
    title: str
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

    @field_validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError('Title field must have a minimun length of 5 chareacters')
        if len(value) > 15:
            raise ValueError('Title field must have a maximun length of 15 chareacters')
        return value

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

# se puede enviar una respuesta HTML hacia el cliente
@app.get('/show', tags=['Movies'])
def home():
    return HTMLResponse('<h1>Show The Batman</h1>')




# Probando el tipo de respuesta de archivo
@app.get('/get_file')
def get_file():
    return FileResponse('file.pdf')