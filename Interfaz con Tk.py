##Hacer una interfaz de usuario libre usando Tk, en una ventana raiz, crea una interfaz de usuario
##que tenga un número de controles (widgets) representativo con respecto a lo que hemos visto en clase
import tkinter as tk

raiz = tk.Tk()

#DEFINICION DE FUNCIONES
def salida():
    raiz.destroy()
    
def crear():
    def pulsar():
        texto=campo1.get()
        mensaje1.destroy()
        campo1.destroy()
        boton1.destroy()
        añadir(texto)

    def añadir(tipodelista):
        mensaje2 = tk.Label(raiz,text=("Lista de "+tipodelista))
        mensaje2.pack(padx=20,pady=10)
        mensaje3.pack(padx=20,pady=10)
        campo2.pack()
        boton2.pack(padx=20,pady=20)
        boton3.pack(padx=20,pady=20)

    def pulsarAñadir():
        texto=campo2.get()
        lista.append(texto)
        print(lista)
        campo2.delete(0,tk.END)

    def pulsarAceptar():
        mensaje3.destroy()
        campo2.destroy()
        boton2.destroy()
        boton3.destroy()
        mensaje4 = tk.Label(raiz,text="Lista creada correctamente")
        mensaje4.pack(padx=20,pady=20)
        print(lista)

    lista = []
    mensaje1 = tk.Label(raiz,text="De qué quieres hacer la lista")
    mensaje1.pack(padx=20,pady=20)
    mensaje3 = tk.Label(raiz,text="Añade un elemento")
    campo1 = tk.Entry(raiz)
    campo1.pack()
    campo2 = tk.Entry(raiz)
    boton1 = tk.Button(raiz,text="Aceptar",command=pulsar)
    boton1.pack(padx=20,pady=20)
    boton2 = tk.Button(raiz,text="Añadir",command=pulsarAñadir)
    boton3 = tk.Button(raiz,text="Aceptar",command=pulsarAceptar)
    return lista

def abrir():
    print(listado)
    

#título de la ventana
raiz.title("Título provisional")
#declaramos la lista
listado = crear()
#Creamos una barra de menu
barramenu = tk.Menu(raiz)
raiz.config(menu=barramenu)

lista = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Lista",menu=lista)

lista.add_command(label="Crear nuevo formulario",command=crear)
lista.add_command(label="Abrir una lista",command=abrir)
lista.add_command(label="Eliminar una lista")

salir = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Salir",menu=salir)

salir.add_command(label="Salir",command=salida)



#Dimesiones de la ventana y localización en pantalla
anchuraventana = 400
alturaventana = 400
anchurapantalla =raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()
esquinax = int(anchurapantalla/2 - anchuraventana/2)
esquinay = int(alturapantalla/2 - alturaventana/2)
raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))
#cambio de icono de la ventana
raiz.iconbitmap("icono.ico")
###---------------------------------------------------
###label
##tk.Label(raiz,text="Hola mundo desde tkinter").pack(padx=50,pady=50)
###boton
##tk.Button(raiz,text="Botón"",command=definir un metodo para poerlo aquí").pack(padx=50,pady=50)
###campo de entrada
##tk.Entry(raiz).pack(padx=50,pady=50)
###checkbutton
##tk.Checkbutton(raiz,text="marcar").pack(padx=50,pady=50)
###radiobutton
##tk.Radiobutton(raiz,text="marcar").pack(padx=50,pady=50)
###lista con elementos
##frutas = ['manzana','pera','plátano','fresa']
##listado = tk.Listbox(raiz)
##for fruta in frutas:
##    listado.insert(tk.END,fruta)
##listado.pack(padx=50,pady=50)



raiz.mainloop()
