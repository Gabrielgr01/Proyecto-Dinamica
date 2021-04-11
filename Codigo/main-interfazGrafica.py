# ...... Imporación de librerias ......

import math
import funciones as f # aquí están las funciones matemáticas creadas
from tkinter import * # para la GUI

# ...... GUI (Interfaz gráfica de usuario) ......

ventana_principal = Tk() # define la ventana
ventana_principal.geometry("800x600") # le da dimensiones a la ventana

# crea el encabezado de la ventana
titulo = Label(ventana_principal, text="Proyecto")
titulo.pack()

    ## carga la imagen del problema
img_problema = PhotoImage(file="..\\15-110 (Hibbeler ed14)_transp.png") 
img_label = Label(ventana_principal, image = img_problema)
img_label.pack()

mainloop() # mantiene las ventanas en ejecución
