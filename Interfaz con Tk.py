import tkinter as tk

raiz = tk.Tk()

#DEFINICION DE FUNCIONES
def salida():
    raiz.destroy()
    
def crear():
    def aceptar():
        nombre = campo1.get()
        apellidos = campo2.get()
        edad = selector.get()
        mensaje4.pack(padx=20,pady=20)
        mensaje1.destroy()
        mensaje2.destroy()
        mensaje3.destroy()
        campo1.destroy()
        campo2.destroy()
        selector.destroy()
        caja1.destroy()
        boton1.destroy()
        boton2.destroy()
        print(nombre,apellidos,edad)

    def borrar():
        campo1.delete(0,tk.END)
        campo2.delete(0,tk.END)
        selector.delete(0,tk.END)
        caja1.deselect()

    mensaje1 = tk.Label(raiz,text="Nombre")
    mensaje1.pack(padx=10,pady=10)
    campo1 = tk.Entry(raiz)
    campo1.pack()
    mensaje2 = tk.Label(raiz,text=("Apellidos"))
    mensaje2.pack(padx=10,pady=10)
    campo2 = tk.Entry(raiz)
    campo2.pack()
    mensaje3 = tk.Label(raiz,text=("Edad"))
    mensaje3.pack(padx=10,pady=10)
    selector = tk.Spinbox(raiz,from_=0,to=100)
    selector.pack()
    caja1 = tk.Checkbutton(raiz,text="Tengo coche")
    caja1.pack()
    boton1 = tk.Button(raiz,text="Aceptar",command=aceptar)
    boton1.pack(padx=10,pady=10)
    boton2 = tk.Button(raiz,text="Borrar",command=borrar)
    boton2.pack(padx=10,pady=10)

def abrir():
    def añadir():
        texto = campo1.get()
        lista.append(texto)
        campo1.delete(0,tk.END)
        print(lista)

    def mostrarlista():
        mensaje2 = tk.Label(raiz,text="Tus aficiones son")
        mensaje2.pack(padx=10,pady=10)
        listado = tk.Listbox(raiz)
        for aficion in lista:
            listado.insert(tk.END,aficion)
        listado.pack()
        
    mensaje4.destroy()
    lista = []
    mensaje1 = tk.Label(raiz,text="Escribe tus aficiones")
    mensaje1.pack(padx=10,pady=10)
    campo1 = tk.Entry(raiz)
    campo1.pack()
    boton1 = tk.Button(raiz,text="Añadir",command=añadir)
    boton1.pack(padx=10,pady=10)
    boton2 = tk.Button(raiz,text="Aceptar",command=mostrarlista)
    boton2.pack(padx=10,pady=10)

#título de la ventana
raiz.title("Formulario y aficiones")
#Declaración mensaje 4
mensaje4 = tk.Label(raiz,text="Lista creada correctamente")
#Creamos una barra de menu
barramenu = tk.Menu(raiz)
raiz.config(menu=barramenu)

encuesta = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Encuesta",menu=encuesta)

encuesta.add_command(label="Nueva encuesta",command=crear)
encuesta.add_command(label="Lista de aficiones",command=abrir)

salir = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Salir",menu=salir)

salir.add_command(label="Salir",command=salida)

#Dimesiones de la ventana y localización en pantalla
anchuraventana = 300
alturaventana = 400
anchurapantalla =raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()
esquinax = int(anchurapantalla/2 - anchuraventana/2)
esquinay = int(alturapantalla/2 - alturaventana/2)
raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))
#cambio de icono de la ventana
raiz.iconbitmap("icono.ico")

raiz.mainloop()
