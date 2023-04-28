from tkinter import *
import interfazusuario as interfaz_usuario
import interfazexperto as interfaz_experto
 
class Principal_Uno(Frame):
    def __init__(self):
        # SE CREA UNA VENTANA PRINCIPAL
        root = Tk()
        super().__init__(root)
        #root.iconbitmap('./img/computer.ico')
        root.title("Sistema experto")
        root.resizable(width=False, height=False)
        self.master = root

        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # TITULOS
        titulo = Label(self, text="Bienvenido al sistema experto.")
        titulo.config(font=("Arial", 18, "bold"), padx=10, pady=10)
        titulo.grid(row=1)
        titulo2= Label(self, text="Para recomendar lugares turisticos")
        titulo2.config(font=("Arial", 17, "bold"), padx=10, pady=10)
        titulo2.grid(row=2)

        #BOTON PARA IR A LA INTERFAZ DE USUARIO
        self.usuario = Button(self, text="Interfaz de Usuario", font=("Arial", 13), width=30, command=interfaz_usuario.InterfazUsuario)
        self.usuario.grid(row=3, padx=10, pady=10)

        #BOTON PARA IR A LA INTERFAZ DE USUARIO EXPERTO
        self.experto = Button(self, text="Interfaz de Usuario Experto", font=("Arial", 13), width=30, command=interfaz_experto.InterfazExperto )
        self.experto.grid(row=4, padx=10, pady=10)
        
        #BOTON PARA SALIR DEL PROGRAMA Y CERRAR LA VENTANA
        self.salir = Button(self, text="Salir", font=("Arial", 13,"bold"), fg="red", width=25, command=self.master.destroy)
        self.salir.grid(row=5, padx=10, pady=10)