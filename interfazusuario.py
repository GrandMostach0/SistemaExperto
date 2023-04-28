from tkinter import *
import json
 
class InterfazUsuario(Frame):
    def __init__(self):
        #SE CREA UNA VENTANA NUEVA
        root = Toplevel()
        super().__init__(root)
        root.title("Interfaz de usuario")
        root.resizable(width=False, height=False)

        #ATRIBUTOS
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(bd=10, relief="raised")
        self.master = root

        #TITULO
        lbl = Label(self, text="Sistema experto para recomendar \nlugares turisticos")
        lbl.config(font=('Comic Sans MS', 13, "bold"), wraplength=380) # Cambiar letra y color del texto
        lbl.place(x=40, y=0)

        #VARIABLES NECESARIOS 
        self.selec = IntVar()
        self.selec2 = IntVar()
        self.selec3 = IntVar()
        self.selec4 = IntVar()

        #ESPACIO VACIO 
        espacio = Label(self, text=" ")
        espacio.grid(row=0, column=0,columnspan=3, pady=5, sticky=SE)
        espacio = Label(self, text=" ")
        espacio.grid(row=1, column=0, columnspan=3, pady=10, sticky=SE)

        # PREGUNTA 1
        self.lbl1 = Label(self, text="Edad:")
        self.lbl1.config(font=('Arial', 11, "bold"))
        self.lbl1.grid(padx=10, row=2, sticky=E)
        radio1 = Radiobutton(self, text="18 - 25 años", font=('Arial', 10), value=1, variable=self.selec).grid(row=2, column=1, sticky=W)
        radio2 = Radiobutton(self, text="26 - 35 años", font=('Arial', 10), value=2, variable=self.selec).grid(row=3, column=1, sticky=W)
        radio3 = Radiobutton(self, text="35 - 40 años", font=('Arial', 10), value=3, variable=self.selec).grid(row=4, column=1, sticky=W)
        #radio4 = Radiobutton(self, text="Edición", font=('Arial', 10), value=4, variable=self.selec).grid(row=5, #column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=5)

        #PREGUNTA 2
        self.lbl2 = Label(self, text="Presupuesto:")
        self.lbl2.config(font=('Arial', 11, "bold"))
        self.lbl2.grid(padx=10, row=6, sticky=E)
        radio4 = Radiobutton(self, text="$0 - $1,000", font=('Arial', 10), value=1, variable=self.selec2).grid(row=6, column=1, sticky=W)
        radio5 = Radiobutton(self, text="$1,000 - $2,000", font=('Arial', 10), value=2, variable=self.selec2).grid(row=7, column=1, sticky=W)
        radio6 = Radiobutton(self, text="$2,000 - $3,000", font=('Arial', 10), value=3, variable=self.selec2).grid(row=8, column=1, sticky=W)
        radio7 = Radiobutton(self, text="$3,000 - $4,000", font=('Arial', 10), value=4, variable=self.selec2).grid(row=9, column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=10)

        #PREGUNTA 3
        self.lbl3 = Label(self, text="Estadía:")
        self.lbl3.config(font=('Arial', 11, "bold"))
        self.lbl3.grid(padx=10, row=11, sticky=E)
        radio8 = Radiobutton(self, text="Pasadia", font=('Arial', 10), value=1, variable=self.selec3).grid(row=11, column=1, sticky=W)
        radio9 = Radiobutton(self, text="Unos dias", font=('Arial', 10), value=2, variable=self.selec3).grid(row=12, column=1, sticky=W)
        radio10 = Radiobutton(self, text="semanas", font=('Arial', 10), value=3, variable=self.selec3).grid(row=13, column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=14)

        #PREGUNTA 4
        self.lbl4 = Label(self, text="Estación:")
        self.lbl4.config(font=('Arial', 11, "bold"))
        self.lbl4.grid(padx=10, row=15, sticky=E)
        radio11 = Radiobutton(self, text="Invierno", font=('Arial', 10), value=1, variable=self.selec4).grid(row=15, column=1, sticky=W)
        radio12 = Radiobutton(self, text="Otoño", font=('Arial', 10), value=2, variable=self.selec4).grid(row=16, column=1, sticky=W)
        radio13 = Radiobutton(self, text="Verano", font=('Arial', 10), value=3, variable=self.selec4).grid(row=17, column=1, sticky=W)
        radio14 = Radiobutton(self, text="Primavera", font=('Arial', 10), value=4, variable=self.selec4).grid(row=18, column=1, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=19)

        #BOTON DE RESPUESTA Y SU RESPECTIVO DESPLIEGUE 
        self.lbl5 = Button(self, text="Respuesta:", command= self.mostrar)
        self.lbl5.config(font=('Arial', 11, "bold"))
        self.lbl5.grid(padx=10, row=19, sticky=E)
        #LABEL DE LA RESPUESTA (TEXTO)
        self.lbl6 = Label(self, text=" ")
        self.lbl6.config(font=('Arial', 10))
        self.lbl6.grid(row=19, column=1, columnspan=2, sticky=W)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=20)

        #LABEL DE LA IMAGEN
        self.lbl7 = Label(self, text="Imagen:")
        self.lbl7.config(font=('Arial', 11, "bold"))
        self.lbl7.grid(row=21, column=0, sticky=E)

        # LABEL DE DONDE SALE LA IMAGEN
        self.lbl8= Label(self)
        self.lbl8.grid(row=21, column=1)

        self.espacio = Label(self, text=" ")
        self.espacio.grid(row=22)

        # BOTONES DE REGRESAR Y DE EXPLICACION
        b = Button(self, text="Explicación", command=self.explicacion)
        b.config(font=('Arial', 11, "bold"), fg="blue")  # bg = color de fondo , fg = color de texto
        b.grid(padx=10, pady=5 , row=25, column=0, sticky=E)

        b2 = Button(self, text="Volver", command=self.master.destroy)
        b2.config(font=('Arial', 11, "bold"), fg="red")
        b2.grid(padx=30, pady=5, row=25, column=2)
        # self.explicacion()

    # METODO DONDE OBTIENE EXPLICACION
    def explicacion(self):
        v2 = Toplevel(self)
        v2.title("Modulo de explicacion")
        v2.geometry("400x400")

        ancho_ventana = 500
        alto_ventana = 280
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        v2.geometry(posicion)

        #configuracion del texto de explicacion
        tex = Label(v2, text=" ", wraplength=500, font=('Arial',11)) # Aqui poner solo la variable que tiene la explicación
        tex.pack(pady=10)
        salir = Button(v2, font=("Arial",11, "bold"), text="Regresar", fg="red", command=v2.destroy)
        salir.pack(pady=15)

        res_op1 = self.selec.get()
        res_op2 = self.selec2.get()
        res_op3 = self.selec3.get()
        res_op4 = self.selec4.get()

        # abirmos el documento del json
        with open('datos.json') as f:
            lista = json.load(f)

            for info in lista['lugar']:
                if (info['op_1'] == res_op1 and info['op_2'] == res_op2 and info['op_3'] == res_op3 and info['op_4'] == res_op4):
                    tex.config(text=info['exp'])
    
    # METODO DONDE SE OBTIENE LA RESPUESTA DEPENDIENDO LO SELECCIONADO
    def respuesta(self):
        if self.selec.get()==1 and self.selec2.get()==1 and self.selec3.get()==1 and self.selec4.get()==3:
            self.lbl6.config(text="Le recomendamos visitar el Puerto de Progreso ubicado en el estado de Yucatán,\nideal para pasarla bien con amigos, paraje o familia.")
            img = PhotoImage(file="./lugares/progreso1.png")
            self.lbl8.config(image= img)
            self.lbl8.image=img

        else:
            self.lbl6.config(text="NO SE TIENE INFORMACION")
            self.lbl8.config(image='')

        if self.selec.get()==3 and self.selec2.get()==1 and self.selec3.get()==2 and self.selec4.get()==4:
            self.lbl6.config(text="")
            img1 = PhotoImage(file="")
            self.lbl8.config(image= img1)
            self.lbl8.image=img1

    #METODO PARA OBTENER INFORMACION Y SABER SI ESTA COINCIDA
    def mostrar(self):
        res_op1 = self.selec.get()
        res_op2 = self.selec2.get()
        res_op3 = self.selec3.get()
        res_op4 = self.selec4.get()
        #abirmos el documento del json
        with open('datos.json') as f:
            lista = json.load(f)

            for info in lista['lugar']:
                if(info['op_1'] == res_op1 and info['op_2'] == res_op2 and info['op_3'] == res_op3 and info['op_4'] == res_op4):
                    self.lbl6.config(text=info['res'])
                    img = PhotoImage(file="./lugares/"+info['img'])
                    self.lbl8.config(image=img)
                    self.lbl8.image = img