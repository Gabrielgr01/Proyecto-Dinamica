# ...... Imporación de librerias ......

import math
import funciones as f # aquí están las funciones matemáticas creadas
from tkinter import * # para la GUI
from tkinter import ttk
from PIL import ImageTk, Image

# ...... Funciones ......

def verProcedimiento():
    m = float(masa.get())
    vt_i = float(v_tan_inicial.get())
    v_n = float(v_normal.get())
    r_i = float(r_inicial.get())
    t_f = float(t_final.get())
    
    r_final = f.radioFinal (r_i, v_n, t_f)
    v_tan_final = f.conservacionH (r_i, m, vt_i, r_final)
    mag_v_final = f.magnitudVector (v_n, v_tan_final)
    trabajo = f.principioU_E (m, vt_i, mag_v_final)

    procedimiento_texto = """Cálculo del radio final:\n
        r("""+str(t_f)+""") = r(0) - Vn * ("""+str(t_f)+""")\n
        r("""+str(t_f)+""") = """+str(r_i)+""" - """+str(v_n)+""" * """+str(t_f)+"""\n
        r("""+str(t_f)+""") = """+str(f.radioFinal(r_i, v_n, t_f))+""" m\n\n
        Conservación de la cantidad de movimiento angular:\n
        (Ho)_(0) = (Ho)_("""+str(t_f)+""")\n
        t(0) * m * Vt (0) = r("""+str(t_f)+""") * m * Vt("""+str(t_f)+""")\n
        """+str(r_i)+"""("""+str(m)+""")("""+str(vt_i)+""") = """+str(r_final)+"""("""+str(m)+""")(Vt_("""+str(t_f)+"""))\n
        Vt("""+str(t_f)+""") = """+str(v_tan_final)+""" m/s\n\n
        Calculando la rapidez (magnitud) del vector velocidad en t = """+str(t_f)+""":\n
        V("""+str(t_f)+""") = raiz((Vn)^2 + (Vt("""+str(t_f)+"""))^2)\n
        V("""+str(t_f)+""") = raiz(("""+str(v_n)+""")^2 + ("""+str(v_tan_final)+""")^2)\n
        V("""+str(t_f)+""") = """+str(mag_v_final)+""" m/s\n\n
        Principio de trabajo y energía:\n
        T(0) + U = T("""+str(t_f)+""")\n
        (1/2)(m)(V(0))^2 + U = (1/2)(m)(V("""+str(t_f)+"""))^2\n
        (1/2)("""+str(m)+""")("""+str(vt_i)+""")^2 + U = (1/2)("""+str(m)+""")("""+str(mag_v_final)+""")^2\n
        U = """+str(trabajo)+""" J\n\n
        Respuesta:\nVelocidad final: """+str(round(mag_v_final, 2))+""" m/s\nTrabajo: """+str(round(trabajo, 2))+""" J"""
    procedimiento["text"] = procedimiento_texto
    b_procedimiento.pack_forget()

#def verGrafica():

    
def calcularProblema():
    m = float(masa.get())
    vt_i = float(v_tan_inicial.get())
    v_n = float(v_normal.get())
    r_i = float(r_inicial.get())
    t_f = float(t_final.get())
    
    #r_final = f.radioFinal (r_i, v_n, t_f)
    #v_tan_final = f.conservacionH (r_i, m, vt_i, r_final)
    #mag_v_final = f.magnitudVector (v_n, v_tan_final)
    #trabajo = f.principioU_E (m, vt_i, mag_v_final)

    resultado_texto = f.calcular(m, vt_i, v_n, r_i, t_f)
    #resultado_texto = "RESULTADO:\nVelocidad final: "+str(mag_v_final)+" m/s\nTrabajo: "+str(trabajo)+" J"
    resultado["text"] = resultado_texto
    #print ("Velocidad final: ", mag_v_final, "\nTrabajo: ", trabajo)

    procedimiento["text"] = ""
    
    b_procedimiento.pack()
    
    #b_grafica = Button (ventana_principal, text="Ver gráfica", command=verGrafica)
    #b_grafica.place(x=200, y=700)


# ...... GUI (Interfaz gráfica de usuario) ......

## Creación de la ventana principal y componentes principales de la interfaz
ventana_principal = Tk() # define la ventana
ventana_principal.title("GABRIEL GONZALEZ R - PROYECTO DINÁMICA")
ventana_principal.geometry("830x600")
#ventana_principal.iconbitmap(default='icon.ico')

main_frame = Frame(ventana_principal)
main_frame.pack(fill=BOTH, expand=1)

main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

### Barra de desplazamiento
main_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
main_scrollbar.pack(side=RIGHT, fill=Y)
main_canvas.configure(yscrollcommand=main_scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

def ruedaRaton(evento): # para que se pueda mover con el ratón
    main_canvas.yview_scroll(-1 * int((evento.delta / 120)), "units")
main_canvas.bind_all("<MouseWheel>", ruedaRaton)

subframe = Frame(main_canvas)
main_canvas.create_window((0,0), window=subframe, anchor="nw")


## Creación de los 'Frames' específicos para cada sección

### Encabezado
f_encabezado = LabelFrame(subframe, text="Encabezado")#, padx=10, pady=10)
f_encabezado.pack(padx=10, pady=10)#padx=10, pady=10)
titulo = Label(f_encabezado, text="""Tecnológico de Costa Rica
    MI3117 - Dinámica - Grupo 03
    Proyecto - Informe 02
    Autor: Gabriel Orlando González Rodríguez
    Carné: 2019057549
    Profesor: Carlos Otárola Zúñiga
    IS - 2021
    """)
titulo.pack() # *agregar texto al encabezado

### Imagen del enunciado
f_imagen = LabelFrame(subframe, text="Problema", padx=10, pady=10)
f_imagen.pack(padx=10, pady=10)

img_problema = PhotoImage(file="..\\15-110 (Hibbeler ed14)_transp.png") 
img_label = Label(f_imagen, image = img_problema)
img_label.pack()

### Para contener los calculos y el procedimiento
f_calculos = LabelFrame(subframe, padx=10, pady=10, bd=0)
f_calculos.pack(padx=10, pady=10)

#### Sección de Procedimiento
f_procedimiento = LabelFrame(f_calculos, text="Procedimiento", padx=10, pady=10)
f_procedimiento.grid(row=0, column=1, padx=10, pady=10)

procedimiento = Label(f_procedimiento)
procedimiento.pack()

#### Para contener la entrada de parámetros , resultado y avisos
f_calculosL = LabelFrame(f_calculos, padx=10, pady=10, bd=0)
f_calculosL.grid(row=0, column=0)

##### Sección de Avisos
f_avisos = LabelFrame(f_calculosL, text="Avisos", padx=10, pady=10)
f_avisos.pack(padx=10, pady=10)

aviso_hola = Label(f_avisos, text="Hola :)")
aviso_hola.pack()
#aviso_calcular = Label(f_avisos)
#aviso_calcular.pack()
#aviso_verProcedimiento = Label(f_avisos)
#aviso_verProcedimiento.pack()
#aviso_verGrafica = Label(f_avisos)
#aviso_verGrafcia.pack()

##### Entrada de datos (ej: 200, 3, 0.5, 8, 4)
f_parametros = LabelFrame(f_calculosL, text="Parámetros de entrada", padx=10, pady=10)
f_parametros.pack(padx=10, pady=10)

datos_t1 = Label(f_parametros, text="""Condiciones iniciales del problema:
    masa=200kg, velocidad tangencial inicial = 3 m/s,
    velocidad normal = 0.5 m/s, radio inicial = 8 m, 
    tiempo final = 4 s\n""")
datos_t1.grid(row=0, column=0, columnspan=2)

l_masa = Label(f_parametros, text="Masa (kg): ", anchor="w")
l_masa.grid(row=1, column=0)
masa = Entry(f_parametros, width=16) # Crea caja de texto
masa.grid(row=1, column=1)

l_vti = Label(f_parametros, text="Velocidad tangencial inicial (m/s): ")
l_vti.grid(row=2, column=0)
v_tan_inicial = Entry(f_parametros, width=16) # Crea caja de texto
v_tan_inicial.grid(row=2, column=1)

l_vn = Label(f_parametros, text="Velocidad normal (m/s): ")
l_vn.grid(row=3, column=0)
v_normal = Entry(f_parametros, width=16) # Crea caja de texto
v_normal.grid(row=3, column=1)

l_ri = Label(f_parametros, text="Radio inicial (m): ")
l_ri.grid(row=4, column=0)
r_inicial = Entry(f_parametros, width=16) # Crea caja de texto
r_inicial.grid(row=4, column=1)

l_tf = Label(f_parametros, text="Tiempo final (s): ")
l_tf.grid(row=5, column=0)
t_final = Entry(f_parametros, width=16) # Crea caja de texto
t_final.grid(row=5, column=1)

##### Sección de Resultado
f_resultado = LabelFrame(f_calculosL, text="Resultado", padx=10, pady=10)
f_resultado.pack(padx=10, pady=10)

resultado = Label(f_resultado)
resultado.pack()

##### Sección de Avisos
f_notas = LabelFrame(f_calculosL, text="Sobre el uso del programa", padx=10, pady=10)
f_notas.pack(padx=10, pady=10)

notas1 = Label(f_notas, text="""1. Si al oprimir algún botón se despliega una sección del
    programa que queda salida de la ventana y no puede
    acceder a ella con la barra de deslizamiento ni con
    el ratón, extienda manualmente la ventana y estos
    se habilitarán de inmediato.\n
    2. Puede probar el programa con cualesquiera valores
    de entrada que desee, las condiciones inciales del
    problema se muestran en pantalla. Ingrese solo valores
    numéricos (no agregue las unidades). 
    """)
notas1.pack()

## Botones
b_resultado = Button(f_parametros, text = "Calcular", command = calcularProblema)
b_resultado.grid(row=6, column=1, pady=10)

b_procedimiento = Button (f_resultado, text="Ver procedimiento", command=verProcedimiento)
#b_procedimiento.place(x=120, y=700)


ventana_principal.mainloop() # mantiene las ventanas en ejecución
