from todor import create_app

# manda a llamar a la configuración del proyecto mediante create_app y 
# con ello se evita de ejecutar el proyecto accediendo al archivo __init__.py
if __name__ == '__main__':
    app = create_app()
    app.run()