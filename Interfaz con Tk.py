##Hacer una interfaz de usuario libre usando Tk, en una ventana raiz, crea una interfaz de usuario
##que tenga un número de controles (widgets) representativo con respecto a lo que hemos visto en clase
import tkinter as tk

#definicion de funciones
def salida():
    raiz.destroy()
    

raiz = tk.Tk()
#título de la ventana
raiz.title("Título provisional")
#Creamos una barra de menu
barramenu = tk.Menu(raiz)
raiz.config(menu=barramenu)

lista = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Lista",menu=lista)

lista.add_command(label="Crear nueva lista")
lista.add_command(label="Abrir una lista")
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
