## Este archivo contiene lo correspondiente a la interfáz grádica de usuario
## (GUI) y funciones relacionadas.
##
## Proyecto Dinámica IS - 2021
## Autor: Gabriel Orlando González Rodríguez - 2019057548

# ...... Imporación de librerias ......

import math
import funciones as f # aquí están las funciones matemáticas creadas
from tkinter import * # para la GUI
from tkinter import ttk # para la GUI
import pandas as pd # para trabajar DataFrames
import matplotlib.pyplot as plt # para graficar

# ...... Funciones ......

# Funciones de validación

def validar ():
    # Función: Valida los datos de entrada y de haber alguno incorrecto
    # despliega un error en pantalla
    #
    # Parámetros: no hay
    #
    # Salida:
    # - Cuando los datos son correctos: lista con los datos validados
    # - Cuando los datos son incorrectos: lista vacía
    #
    aviso_calcular ["text"] = "Aquí aparecerán los avisos de error"
    paramList = []
    
    try:
        m = float(masa.get())
        vt_i = float(v_tan_inicial.get())
        v_n = float(v_normal.get())
        r_i = float(r_inicial.get())
        t_f = float(t_final.get())
        
        r_final = f.radioFinal (r_i, v_n, t_f)

        if ((m < 0) or (vt_i < 0) or (v_n < 0) or (r_i < 0) or (t_f < 0)):
            aviso_calcular ["text"] = """ERROR al leer los datos: Revise los valores ingresados.\n
        - Ingrese solo valores positivos"""
            resultado["text"] = ""
            procedimiento["text"] = ""
            b_procedimiento.pack_forget()
            b_graficaVelocidad.pack_forget()
            b_graficaTrabajo.pack_forget()
            b_graficasJuntas.pack_forget()
        elif (r_final <= 0):
            while (r_final <= 0):
                r_final = f.radioFinal (r_i, v_n, t_f)
                t_f -= 0.5
            aviso_calcular ["text"] = """ERROR al leer los datos: Revise los valores ingresados.\n
        - El carrito ya se habría detenido desde que t = """+str(t_f+1)+""" s.
        Ingrese un tiempo menor o igual a """+str(t_f)+""" s, de lo contrarío
        se estaría utilizando un radio final negativo o con valor cero."""
            resultado["text"] = ""
            procedimiento["text"] = ""
            b_procedimiento.pack_forget()
            b_graficaVelocidad.pack_forget()
            b_graficaTrabajo.pack_forget()
            b_graficasJuntas.pack_forget()
        else:
            paramList = [m, vt_i, v_n, r_i, t_f]

    except:
        aviso_calcular ["text"] = """ERROR al leer los datos: Revise los valores ingresados.\n
        - Ingrese solo valores numéricos
        - No deje espacios en blanco
        - Ingrese valores  con sentido físico
        (ej. no puede haber un radio negativo)
        """
        resultado["text"] = ""
        procedimiento["text"] = ""
        b_procedimiento.pack_forget()
        b_graficaVelocidad.pack_forget()
        b_graficaTrabajo.pack_forget()
        b_graficasJuntas.pack_forget()
       
    return paramList


# Funciones al presionar botones

def verProcedimiento():
    # Función: Calcula el problema y despliega el procedimiento en pantalla
    #
    # Parámetros: no hay
    #
    # Salida: no hay
    #

    # Calculos
    m = float(masa.get())
    vt_i = float(v_tan_inicial.get())
    v_n = float(v_normal.get())
    r_i = float(r_inicial.get())
    t_f = float(t_final.get())
    
    r_final = f.radioFinal (r_i, v_n, t_f)
    v_tan_final = f.conservacionH (r_i, m, vt_i, r_final)
    mag_v_final = f.magnitudVector (v_n, v_tan_final)
    trabajo = f.principioU_E (m, vt_i, mag_v_final)

    # Se despliega el texto
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
        Respuesta:\nRapidez final: """+str(round(mag_v_final, 2))+""" m/s\nTrabajo: """+str(round(trabajo, 2))+""" J"""
    procedimiento["text"] = procedimiento_texto
    b_procedimiento.pack_forget() # Deshabilita el botón de ver procedimiento

def verGraficasJuntas():
    # Función: Despliega la gráfica de rapidez y trabajo en función del tiempo
    #
    # Parámetros: no hay
    #
    # Salida: no hay
    #
    listaParam = validar()
    
    if listaParam:   
        plt.close('all')

        df = f.dataFrameCM(listaParam[0], listaParam[1], listaParam[2], listaParam[3], listaParam[4])

        plt.plot(df.tiempo_s, df.velocidad_cm_s, color='r', label="Rapidez final (cm/s)")
        plt.plot(df.tiempo_s, df.trabajo_J, color='b', label="Trabajo (J)")
        plt.legend()
        plt.title("Gráfica de rapídez y trabajo vs tiempo")
        plt.xlabel("Tiempo (s)")
        plt.show()

def verGraficaVelocidad():
    # Función: Despliega la gráfica de rapidez en función del tiempo
    #
    # Parámetros: no hay
    #
    # Salida: no hay
    #
    listaParam = validar()
    
    if listaParam:   
        plt.close('all')
        
        df = f.dataFrame(listaParam[0], listaParam[1], listaParam[2], listaParam[3], listaParam[4])

        plt.plot(df.tiempo_s, df.velocidad_m_s, color='r')
        plt.title("Gráfica de rapidez vs tiempo")
        plt.ylabel("Rapidez (m/s)")
        plt.xlabel("Tiempo (s)")
        plt.show()

def verGraficaTrabajo():
    # Función: Despliega la gráfica de trabajo en función del tiempo
    #
    # Parámetros: no hay
    #
    # Salida: no hay
    #
    listaParam = validar()
    
    if listaParam:    
        plt.close('all')
        
        df = f.dataFrame(listaParam[0], listaParam[1], listaParam[2], listaParam[3], listaParam[4])

        plt.plot(df.tiempo_s, df.trabajo_J, color='b')
        plt.title("Gráfica de trabajo vs tiempo")
        plt.ylabel("Trabajo (J)")
        plt.xlabel("Tiempo (s)")
        plt.show()


def calcularProblema():
    # Función: Calcula el resultado del problema y lo despliega en pantalla
    #
    # Parámetros: no hay
    #
    # Salida: no hay
    #
    listaParam = validar()
    
    if listaParam:
        resultado_texto = f.calcular(listaParam[0], listaParam[1], listaParam[2], listaParam[3], listaParam[4])
        resultado["text"] = resultado_texto
        procedimiento["text"] = ""

        # Deshabilita los botones (para que se reinicien los valores)
        b_procedimiento.pack_forget()
        b_graficaVelocidad.pack_forget()
        b_graficaTrabajo.pack_forget()
        b_graficasJuntas.pack_forget()

        # Habilita los botones
        b_procedimiento.pack(pady=5)
        b_graficaVelocidad.pack(pady=5)
        b_graficaTrabajo.pack(pady=5)
        b_graficasJuntas.pack(pady=5)

            

# ...... GUI (Interfaz gráfica de usuario) ......

## Creación de la ventana principal y componentes principales de la interfaz
ventana_principal = Tk() # define la ventana
ventana_principal.title("GABRIEL GONZALEZ R - PROYECTO DINÁMICA") #Titulo
ventana_principal.geometry("830x600") # Tamaño de la ventana

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
f_encabezado.pack(fill=BOTH, padx=20, pady=10)#padx=10, pady=10)
titulo = Label(f_encabezado, text="""Tecnológico de Costa Rica
MI3117 - Dinámica - Grupo 03
Proyecto - Informe 02
Autor: Gabriel Orlando González Rodríguez
Carné: 2019057549
Profesor: Carlos Otárola Zúñiga
IS - 2021""", justify="left")
titulo.pack(side=LEFT, padx=10, pady=10) # *agregar texto al encabezado


### Imagen del enunciado
f_imagen = LabelFrame(subframe, text="Problema")
f_imagen.pack(padx=20, pady=10)

img_problema = PhotoImage(file="..\\15-110 (Hibbeler ed14)_transp.png") 
img_label = Label(f_imagen, image = img_problema)
img_label.pack()


### Para contener los calculos y el procedimiento
f_calculos = LabelFrame(subframe, bd=0)
f_calculos.pack(fill=BOTH, padx=10, pady=10)

#### Sección de Procedimiento
f_procedimiento = LabelFrame(f_calculos, text="Procedimiento")
f_procedimiento.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

procedimiento = Label(f_procedimiento)
procedimiento.pack(padx=10, pady=10)


#### Para contener la entrada de parámetros , resultado y avisos
f_calculosL = LabelFrame(f_calculos, bd=0)
f_calculosL.grid(row=0, column=0, sticky="nsew", padx=10)

##### Sección de Notas del uso del programa
f_notas = LabelFrame(f_calculosL, text="Sobre el uso del programa")
f_notas.pack(fill=BOTH, pady=5)

notas1 = Label(f_notas, text="""1. Si al oprimir algún botón se despliega una sección del
    programa que queda salida de la ventana y no puede
    acceder a ella con la barra de deslizamiento ni con el
    ratón, extienda manualmente la ventana y estos se
    habilitarán de inmediato.""", justify="left")
notas1.pack(padx=10, pady=10)


##### Sección de Avisos
f_avisos = LabelFrame(f_calculosL, text="Avisos")
f_avisos.pack(fill=BOTH, pady=5)

aviso_calcular = Label(f_avisos, text="Aquí aparecerán los avisos de error", justify="left")
aviso_calcular.pack(padx=10, pady=10)


##### Entrada de datos
f_parametros = LabelFrame(f_calculosL, text="Parámetros de entrada")
f_parametros.pack(fill=BOTH, pady=5)

datos_t1 = Label(f_parametros, text="""Condiciones iniciales del problema:
    masa=200kg, velocidad tangencial inicial = 3 m/s,
    velocidad normal = 0.5 m/s, radio inicial = 8 m, 
    tiempo final = 4 s\n""", justify="left")
datos_t1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

###### Ingreso de los parametros de entrada (ej: 200, 3, 0.5, 8, 4. Respectivamente.)
l_masa = Label(f_parametros, text="Masa (kg): ")
l_masa.grid(sticky= E, row=1, column=0)
masa = Entry(f_parametros, width=16) # Crea caja de texto para la masa
masa.grid(row=1, column=1)

l_vti = Label(f_parametros, text="Velocidad tangencial inicial (m/s): ")
l_vti.grid(sticky= E,row=2, column=0)
v_tan_inicial = Entry(f_parametros, width=16) # Crea caja de texto para la velocidad tangencial inicial
v_tan_inicial.grid(row=2, column=1)

l_vn = Label(f_parametros, text="Velocidad normal (m/s): ")
l_vn.grid(sticky= E,row=3, column=0)
v_normal = Entry(f_parametros, width=16) # Crea caja de texto para la velocidad normal
v_normal.grid(row=3, column=1)

l_ri = Label(f_parametros, text="Radio inicial (m): ")
l_ri.grid(sticky= E,row=4, column=0)
r_inicial = Entry(f_parametros, width=16) # Crea caja de texto para el radio inicial
r_inicial.grid(row=4, column=1)

l_tf = Label(f_parametros, text="Tiempo final (s): ")
l_tf.grid(sticky= E,row=5, column=0)
t_final = Entry(f_parametros, width=16) # Crea caja de texto para el tiempo final deseado
t_final.grid(row=5, column=1)


##### Sección de Resultado
f_resultado = LabelFrame(f_calculosL, text="Resultado")
f_resultado.pack(fill=BOTH, pady=5)

resultado = Label(f_resultado)
resultado.pack()


## Botones
b_resultado = Button(f_parametros, text = "Calcular", command = calcularProblema)
b_resultado.grid(row=6, column=1, pady=10)

b_procedimiento = Button (f_resultado, text="Ver procedimiento", command=verProcedimiento)
b_graficasJuntas = Button (f_resultado, text="Ver Gráficas (Juntas)", width=20, command=verGraficasJuntas)
b_graficaVelocidad = Button (f_resultado, text="Ver Gráfica de Rapidez", width=20, command=verGraficaVelocidad)
b_graficaTrabajo = Button (f_resultado, text="Ver Gráfica de Trabajo", width=20, command=verGraficaTrabajo)


ventana_principal.mainloop() # mantiene las ventanas en ejecución
