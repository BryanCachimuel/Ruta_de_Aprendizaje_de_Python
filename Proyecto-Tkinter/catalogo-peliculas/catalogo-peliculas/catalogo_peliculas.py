import tkinter as tk
from client.gui_app import Frame, barra_menu

"""
Creación de la venta
"""
def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0)                # renderizado de la ventana
    barra_menu(root)

    # Importanto del frame
    app = Frame(root=root)

    app.mainloop()   # todo el código de la proyecto ba antes de está linea

if __name__ == "__main__":
    main()