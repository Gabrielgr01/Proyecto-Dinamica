# ...... Imporación de librerias ......

import math
import funciones as f # aquí están las funciones matemáticas creadas
from tkinter import * # para la GUI

# ...... GUI (Interfaz gráfica de usuario) ......

ventana_principal = Tk() # define la ventana
ventana_principal.geometry("800x600") # le da dimensiones a la ventana
ventana_principal.title("GABRIEL GONZALEZ R - PROYECTO DINÁMICA")
#ventana_principal.iconbitmap(default='icon.ico')


# crea el encabezado de la ventana
titulo = Label(ventana_principal, text="Proyecto")
titulo.pack()

    ## carga la imagen del problema
img_problema = PhotoImage(file="..\\15-110 (Hibbeler ed14)_transp.png") 
img_label = Label(ventana_principal, image = img_problema)
img_label.pack()

# para ingresar los datos (ej: 200, 3, 0.5, 8, 4)
datos_t1 = Label(ventana_principal, text="Ingrese los siguientes valores (constantes): ")
datos_t1.place(x=50, y=460)

l_masa = Label(ventana_principal, text="Masa (kg): ")
l_masa.place(x=50, y=500)
masa = Entry(ventana_principal, width=16) # Crea caja de texto
masa.place(x=120, y=500) # Posicionarla en la ventana

l_vti = Label(ventana_principal, text="Velocidad tangencial inicial (m/s): ")
l_vti.place(x=50, y=540)
v_tan_inicial = Entry(ventana_principal, width=16) # Crea caja de texto
v_tan_inicial.place(x=240, y=540) # Posicionarla en la ventana

l_vn = Label(ventana_principal, text="Velocidad normal (m/s): ")
l_vn.place(x=50, y=580)
v_normal = Entry(ventana_principal, width=16) # Crea caja de texto
v_normal.place(x=190, y=580) # Posicionarla en la ventana

l_ri = Label(ventana_principal, text="Radio inicial (m): ")
l_ri.place(x=50, y=620)
r_inicial = Entry(ventana_principal, width=16) # Crea caja de texto
r_inicial.place(x=150, y=620) # Posicionarla en la ventana

l_tf = Label(ventana_principal, text="Tiempo final (s): ")
l_tf.place(x=50, y=660)
t_final = Entry(ventana_principal, width=16) # Crea caja de texto
t_final.place(x=150, y=660) # Posicionarla en la ventana


# Sección de resultado
resultado = Label(ventana_principal)
resultado.place(x=50, y=740)

def calcularProblema():
    m = float(masa.get())
    vt_i = float(v_tan_inicial.get())
    v_n = float(v_normal.get())
    r_i = float(r_inicial.get())
    t_f = float(t_final.get())
    
    r_final = f.radioFinal (r_i, v_n, t_f)
    v_tan_final = f.conservacionH (r_i, m, vt_i, r_final)
    mag_v_final = f.magnitudVector (v_n, v_tan_final)
    trabajo = f.principioU_E (m, vt_i, mag_v_final)

    resultado_texto = "Velocidad final: "+str(mag_v_final)+" m/s\nTrabajo: "+str(trabajo)+" J"
    resultado["text"] = resultado_texto
    #print ("Velocidad final: ", mag_v_final, "\nTrabajo: ", trabajo)

b_resultado = Button(ventana_principal, text = "Calcular", command = calcularProblema)
b_resultado.place(x=50, y=700)


mainloop() # mantiene las ventanas en ejecución
