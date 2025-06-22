from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, Response, JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.requests import Request

# Importando el motor de plantilla jinja2
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# mandando a llamar al middleware de control de errores
#app.add_middleware(HTTPErrorHandler)
@app.middleware('http')
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    print('Middleware is running')
    return await call_next(request)

# definir donde van a estar ubicados los archivos estáticos y archivos template
static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

app.mount('/static', StaticFiles(directory=static_path), 'static')
templates = Jinja2Templates(directory=templates_path)

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


# incluyendo las rutas del archivo movie_router
app.include_router(prefix='/movies', router=movie_router)


# Formas de uso del método get y sus tipos de respuesta en el retorno que se puede tener

# se puede enviar una respuesta HTML hacia el cliente
@app.get('/show', tags=['Movies'])
def home():
    return HTMLResponse('<h1>Show The Batman</h1>')

# Probando el tipo de respuesta de archivo
@app.get('/get_file')
def get_file():
    return FileResponse('file.pdf')