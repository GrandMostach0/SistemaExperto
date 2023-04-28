from tkinter import *
from tkinter import filedialog
import llenarDatos as llenar

import json
##libreria de manejador de archivos
import shutil
import os

class InterfazExperto(Frame):
    def __init__(self):
        #CREACION DE LA VENTANA
        root = Toplevel()
        super().__init__(root)
        #root.iconbitmap("ruta imagen aqui con extencion .ico")
        root.title("Modulo para agregar mas conocimiento")
        root.resizable(width=False, height=False)

        #ATRIBUTOS DE LA PROPIEDAD GRID
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #BD = TAMAÑO DEL BORDE, RELIEF = ESTILO DEL BORDE
        self.config(bd=10, relief="raised")
        self.master = root

        #TITULO DE LA VENTANA CON UN ESTILO DIFERENTE
        lbl = Label(self, text="Módulo de adiquisición de conocimiento")
        #ATRIBUTOS DEL LABEL PARA CAMBIARLE EL FONT,SIZE Y ESTILO
        lbl.config(font=('Comic Sans MS', 15, "bold"))
        lbl.place(x=28, y=0)

        #VARIABLES PARA BUSCAR LA RESPUESTA
        self.selec = IntVar()
        self.selec2 = IntVar()
        self.selec3 = IntVar()
        self.selec4 = IntVar()
        self.imageName = StringVar()

        #ESPACIO VACIO
        espacio = Label(self, text=" ")
        espacio.grid(row=0, column=0,columnspan=3, pady=10, sticky=SE)

        # PREGUNTA 1
        self.lbl1 = Label(self, text="Edad:")
        self.lbl1.config(font=('Arial', 11, "bold"))
        self.lbl1.grid(padx=10, row=1, sticky=E)
        radio1 = Radiobutton(self, text="18 - 25 años", font=('Arial', 10), value=1, variable=self.selec).grid(row=1, column=1, sticky=W)
        radio2 = Radiobutton(self, text="26 - 35 años", font=('Arial', 10), value=2, variable=self.selec).grid(row=2, column=1, sticky=W)
        radio3 = Radiobutton(self, text="35 - 40 años", font=('Arial', 10), value=3, variable=self.selec).grid(row=3, column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=4)

        #PREGUNTA 2
        self.lbl2 = Label(self, text="Presupuesto: ")
        self.lbl2.config(font=('Arial', 11, "bold"))
        self.lbl2.grid(padx=10, row=5, sticky=E)
        radio5 = Radiobutton(self, text="$0 - $1,000", font=('Arial', 10), value=1, variable=self.selec2).grid(row=5, column=1, sticky=W)
        radio6 = Radiobutton(self, text="$1,000 - $2,000", font=('Arial', 10), value=2, variable=self.selec2).grid(row=6, column=1, sticky=W)
        radio7 = Radiobutton(self, text="$2,000 - $3,000", font=('Arial', 10), value=3, variable=self.selec2).grid(row=7, column=1, sticky=W)
        radio8 = Radiobutton(self, text="$3,000 - $4,000", font=('Arial', 10), value=4, variable=self.selec2).grid(row=8, column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=9)

        #PREGUNTA 3
        self.lbl3 = Label(self, text="Estadía:")
        self.lbl3.config(font=('Arial', 11, "bold"))
        self.lbl3.grid(padx=10, row=10, sticky=E)
        radio9 = Radiobutton(self, text="Pasadia", font=('Arial', 10), value=1, variable=self.selec3).grid(row=10, column=1, sticky=W)
        radio10 = Radiobutton(self, text="Unos dias", font=('Arial', 10), value=2, variable=self.selec3).grid(row=11, column=1, sticky=W)
        radio11 = Radiobutton(self, text="Semanas", font=('Arial', 10), value=3, variable=self.selec3).grid(row=12, column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=13)

        #PREGUNTA 4
        self.lbl4 = Label(self, text="Estación:")
        self.lbl4.config(font=('Arial', 11, "bold"))
        self.lbl4.grid(padx=10, row=14, sticky=E)
        radio12 = Radiobutton(self, text="Invierno", font=('Arial', 10), value=1, variable=self.selec4).grid(row=14, column=1, sticky=W)
        radio13 = Radiobutton(self, text="Otoño", font=('Arial', 10), value=2, variable=self.selec4).grid(row=15, column=1, sticky=W)
        radio14 = Radiobutton(self, text="Verano", font=('Arial', 10), value=3, variable=self.selec4).grid(row=16, column=1, sticky=W)
        radio15 = Radiobutton(self, text="Primavera", font=('Arial', 10), value=4, variable=self.selec4).grid(row=17, column=1, sticky=W)

        #LABEL PARA RESPUESTA
        self.lbl5 = Label(self, text="Respuesta:")
        self.lbl5.config(font=('Arial', 11, "bold"))
        self.lbl5.grid(padx=15, row=18, pady=15, sticky=E)

        # PARA INSERTAR LA RESPUESTA
        self.lbl6 = Text(self, width=45, height=2)
        self.lbl6.config(font=('Arial', 9))
        self.lbl6.grid(row=18, column=1, columnspan=2, sticky=W)

        #LABEL PARA EXPLICACIÓN
        self.lbl7 = Label(self, text="Explicación:")
        self.lbl7.config(font=('Arial', 11, "bold"))
        self.lbl7.grid(padx=10, row=19, pady=5, sticky=E)

        # PARA INSERTAR EXPLICACION
        self.lbl8 = Text(self, width=45, height=5)
        self.lbl8.config(font=('Arial', 9))
        self.lbl8.grid(row=19, column=1, columnspan=2, sticky=W)

        #LABEL PARA IMAGEN
        self.lbl9 = Label(self, text="Imagen:")
        self.lbl9.config(font=('Arial', 11, "bold"))
        self.lbl9.grid(row=20, column=0, pady=15, padx=10, sticky=E)

        # BOTON PARA SUBIR IMAGEN
        self.lbl20= Button(self, text="Subir", command=self.browseFiles)
        self.lbl20.config(font=('Arial', 11, "bold"))
        self.lbl20.grid(row=20, column=1, sticky=W)

        # BOTONES DE REGRESAR Y GUARDAR
        b = Button(self, text="Guardar", command=self.initBaseDatos)
        b.config(font=('Arial', 11, "bold", "italic"), fg="blue")  # bg = color de fondo , fg = color de texto
        b.grid(row=21, column=0, sticky=E)

        b2 = Button(self, text="Regresar", command=self.master.destroy)
        b2.config(font=('Arial', 11, "bold"), fg="red")
        b2.grid(padx=60, pady=5, row=22, column=2)


    # METODO PARA ABRIR EL EXPLORADOR DE ARRCHIVOS Y SELECIONAR UNA IMAGEN Y OBTNER LA RUTA
    def browseFiles(self):
        filename = filedialog.askopenfilename(
            initialdir = "/",
            title = "Selecciona un archivo",
            filetypes = (("Imagen png", "*.png*"),("Imagen gif", "*.gif*"),("Todos los archivos", "*.*")))
        self.lbl20.configure(text="Archivo subido: "+ os.path.basename(filename))
        self.imageName = filename

    def initBaseDatos(self):
        #FUNCION PARA RECUPERAR LA INFORMACION
        opcion_1 = self.selec.get()
        opcion_2 = self.selec2.get()
        opcion_3 = self.selec3.get()
        opcion_4 = self.selec4.get()
        respuesta = self.lbl6.get("1.0", END)
        explicacion = self.lbl8.get("1.0", END)
        imagenRuta = self.imageName
        imagen = os.path.basename(imagenRuta)

        ##funcion en un try catch por si ocurre algun error
        try:
            if (opcion_1 == 0 or opcion_2 == 0 or opcion_3 == 0 or opcion_4 == 0 or len(respuesta) == 1 or len(explicacion) == 1 or len(imagen) == 1 or len(imagen) == 0):
                print('algunos campos estan vacios')
            else :

                rutaDestino = "./lugares"

                #diccionario que luego se convertira en un json
                x = {
                    'op_1': opcion_1,
                    'op_2': opcion_2,
                    'op_3': opcion_3,
                    'op_4': opcion_4,
                    'res': respuesta,
                    'exp': explicacion,
                    'img': imagen
                }

                # FUNCION EXTERNO QUE REALIZA LA INSECION EN EL DOCUMENTO
                llenar.write_json(x)

                #FUNCION PARA MOVER LA IMAGEN A LA CARPETA DE IMAGENES
                shutil.copy(imagenRuta, rutaDestino)

                #esta linea de codigo sirve para "borrar" los datos colocados o seleccionados en el menu
                self.selec.set(0)
                self.selec2.set(0)
                self.selec3.set(0)
                self.selec4.set(0)
                self.lbl6.delete("1.0", END)
                self.lbl8.delete("1.0", END)
        except:
            print('error')