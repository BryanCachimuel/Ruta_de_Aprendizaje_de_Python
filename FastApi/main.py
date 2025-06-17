from fastapi import FastAPI

app = FastAPI()

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
