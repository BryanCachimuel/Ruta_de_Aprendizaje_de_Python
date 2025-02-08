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

        # diseñando los entrys o campos de entrada
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, state='disabled', font=('Arial',12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, state='disabled', font=('Arial',12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, state='disabled', font=('Arial',12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones
        self.boton_nuevo = tk.Button(self, text="Nuevo")
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), 
                                fg='#DAD5D6', 
                                bg='#158645', 
                                cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4, column=0,padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar")
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), 
                                fg='#DAD5D6', 
                                bg='#1658A2', 
                                cursor='hand2',
                                activebackground='#3586DF')
        self.boton_guardar.grid(row=4, column=1,padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar")
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), 
                                fg='#DAD5D6', 
                                bg='#BD152E', 
                                cursor='hand2',
                                activebackground='#E15370')
        self.boton_cancelar.grid(row=4, column=2,padx=10, pady=10)