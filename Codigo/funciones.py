# ......importación de librerias......
import math
import pandas as pd



def int_a_float(valor):
    if (type(valor) == int):
        valor_float = float(valor)
    elif (type(valor) == float):
        valor_float = valor
    else:
        print("Error: Ingrese un valor numérico")


# ......Funciones para los cálculos del problema......

def radioFinal (r_inicial, v_normal, t_final):
    # Función: Calcula el radio final del cable
    #
    # Parámetros:
    # r_inicial: radio inicial del cable.
    # v_normal: velocidad normal (constante)
    # t_final: tiempo que se toma como final para el análisis
    #
    # Salida:
    # r_final: radio al final del recorrido
    # 
    r_final = r_inicial - v_normal * t_final
    return r_final

def conservacionH (r_inicial, masa, v_tan_inicial, r_final):
    # Función: Calcula la velocidad tangencial final aplicando la
    # consevación de la cantidad de movimiento lineal.
    #
    # Parámentros:
    # r_inicial: radio inicial del cable.
    # masa: masa del carrito
    # r_final: radio al final del período de tiempo considerado
    #
    # Salida:
    # v_tan_final: velocidad tangencial al final del recorrido
    #
    v_tan_final = (r_inicial * v_tan_inicial)/r_final
    return v_tan_final

def magnitudVector (a, b):
    # Función: Calcula la magnitud de un vector dadas sus componentes
    #
    # Parámetros:
    # a y b: componentes del vector
    #
    # Salida:
    # magnitud: magnitud del vector
    #
    magnitud = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return magnitud

def principioU_E (masa, v_inicial, v_final):
    # Función: Calcula el trabajo realizado aplicando el principio de
    # trabajo y energía dadas la masa, la velocidad inicial y la
    # velocidad final
    #
    # Parámetros:
    # masa: masa del carrito
    # v_inicial: velocidad incial del carrito
    # v_final: velocidad final del carrito
    #
    # Salida:
    # U: trabajo realizado readoneado a dos decimales
    #
    U = (masa * math.pow(v_final, 2))/2 - (masa * math.pow(v_inicial, 2))/2
    U_redondeado = round(U, 2)
    return U_redondeado


def calcular(masa, v_tan_inicial, v_normal, r_inicial, t_final):
    r_final = radioFinal (r_inicial, v_normal, t_final)
    v_tan_final = conservacionH (r_inicial, masa, v_tan_inicial, r_final)
    mag_v_final = magnitudVector (v_normal, v_tan_final)
    trabajo = principioU_E (masa, v_tan_inicial, mag_v_final)

    return("Velocidad final: "+str(round(mag_v_final, 2))+" m/s\nTrabajo: "+str(round(trabajo, 2))+" J")


## ...... Para Graficar ......

##def dataFrames(masa, v_tan_inicial, v_normal, r_inicial, t_final):
##
##    df_velocidad = pd.DataFrame(columns=["Tiempo (s)","Velocidad (m/s)"])
##    df_trabajo = pd.DataFrame(columns=["Tiempo (s)","Trabajo (J)"])
##    
##    if (t_final%2 == 0):
##        rango = t_final+t_final+1
##    else:
##        rango = t_final+t_final+1
##    
##    for i in range(rango):
##        try:
##            r_final = radioFinal (r_inicial, v_normal, i)
##            v_tan_final = conservacionH (r_inicial, masa, v_tan_inicial, r_final)
##            mag_v_final = magnitudVector (v_normal, v_tan_final)
##            trabajo = principioU_E (masa, v_tan_inicial, mag_v_final)
##
##            df_velocidad.loc[i] = [i, mag_v_final]
##            df_trabajo.loc[i] = [i, trabajo]
##
##        except ZeroDivisionError:
##            break
##        
##    # print: Para revisar los dataFrames
##    print(df_velocidad)
##    print("\n")
##    print(df_trabajo)


def dataFrame(masa, v_tan_inicial, v_normal, r_inicial, t_final):

    df = pd.DataFrame(columns=["tiempo_s","velocidad_m_s","trabajo_J"])
    
    if (t_final%2 == 0):
        rango = t_final+t_final+1
    else:
        rango = t_final+t_final+1
    
    for i in range(int(rango)):
        try:
            r_final = radioFinal (r_inicial, v_normal, i)
            v_tan_final = conservacionH (r_inicial, masa, v_tan_inicial, r_final)
            mag_v_final = magnitudVector (v_normal, v_tan_final)
            trabajo = principioU_E (masa, v_tan_inicial, mag_v_final)

            df.loc[i] = [i, mag_v_final, trabajo]

        except ZeroDivisionError:
            break
    return df        
    ## print: Para revisar el dataFrame
    #print(df)

def dataFrameCM(masa, v_tan_inicial, v_normal, r_inicial, t_final):

    df = pd.DataFrame(columns=["tiempo_s","velocidad_cm_s","trabajo_J"])
    
    if (t_final%2 == 0):
        rango = t_final+t_final+1
    else:
        rango = t_final+t_final+1
    
    for i in range(int(rango)):
        try:
            r_final = radioFinal (r_inicial, v_normal, i)
            v_tan_final = conservacionH (r_inicial, masa, v_tan_inicial, r_final)
            mag_v_final = magnitudVector (v_normal, v_tan_final)
            trabajo = principioU_E (masa, v_tan_inicial, mag_v_final)

            df.loc[i] = [i, mag_v_final*100, trabajo]

        except ZeroDivisionError:
            break
    return df        
    ## print: Para revisar el dataFrame
    #print(df)
