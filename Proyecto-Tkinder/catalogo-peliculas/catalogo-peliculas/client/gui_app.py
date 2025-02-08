import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    # Inicio
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    # submenus de inicio
    menu_inicio.add_command(label='Crear Registro en BD')
    menu_inicio.add_command(label='Eliminar Registro en BD')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        #self.config(bg='green')

        self.campos_pelicula()

    # labels para agregar una pelicula
    def campos_pelicula(self):
        # labels de cada campo
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial',12,'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Género: ')
        self.label_genero.config(font=('Arial',12,'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)