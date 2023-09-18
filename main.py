# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 12:12:14 2019
@author: Gustavo Rdz
"""

#Import modules
import tkinter as tk 
import pandas as pd
from tkinter import filedialog
from tkinter import scrolledtext
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global save


#Crear instancia
root = tk.Tk()


#Funciones
def getCSV():
    global sample_data
    global import_file_path
    global algo
    
    import_file_path = filedialog.askopenfilename()
    sample_data = pd.read_csv (import_file_path,header=None, sep='\t')
    sample_data = sample_data[0].str.split(',', expand=True)
    text1 = tk.Text(frame1, font=10)
    text1.place(relwidth=0.70, relheight=1)
    text1.insert(tk.INSERT, import_file_path)

def exportCSV():
    global save
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    save.to_csv (export_file_path, index = None, header=True)
    text_save = tk.Text(frame4, font=10)
    text_save.place(relwidth=0.70, relheight=1)
    text_save.insert(tk.INSERT, export_file_path) 

def getTempmax():
    global save
    ### LOG 3 ###
    #TEMPERATURAS
    log_data_3 = sample_data[sample_data[4] == "Log_3"]
    log_data_3 = log_data_3.iloc[:, 0:12]
    log_data_3.columns = ['MAC','FECHA','HORA','STATUS','LOG','T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']
    log_data_3 = log_data_3.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_3[['T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']] = log_data_3[['T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']].astype('int8')
    log_data_3['FECHA'] = pd.to_datetime(log_data_3['FECHA'])

    resultados = []
    i = 0

    # Itera a través de las columnas
    for columna in ['T_M1', 'T_M2', 'T_M3', 'T_M4',	'T_M5', 'T_M6',	'T_M7']:

        # Encuentra la temperatura máxima y su índice (hora) correspondiente
        max_temp = log_data_3[columna].max()
        hora_max_temp = log_data_3[log_data_3[columna] == max_temp]['HORA'].values[0]
        
        # Agrega los resultados a la lista
        lista = ['1', '2', '3', '4', '5', '6', '7']
        resultados.append((lista[i], max_temp, hora_max_temp))
        i = i + 1

    # Convierte la lista de resultados en un DataFrame
    temps_max = pd.DataFrame(resultados, columns=['Modulo', 'Temp', 'Hora'])
    save = temps_max
    ttext = tk.Text(frame3, font=("Calibri", 20))
    ttext.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
    ttext.insert(tk.INSERT, temps_max)

def Tempmaxinfo():
    global save
    ### LOG 1 ###
    #VDC, GRID, ICS
    log_data_1 = sample_data[sample_data[4] == "Log_1"]
    log_data_1 = log_data_1.iloc[:,0:17]
    log_data_1.columns = ['MAC','FECHA','HORA','STATUS','LOG','DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
                        'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']
    log_data_1 = log_data_1.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_1[['DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
            'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']] = log_data_1[['DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
            'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']].astype('int16') 
    log_data_1['FECHA'] = pd.to_datetime(log_data_1['FECHA'])
    log_data_1['FREQ'] = log_data_1['FREQ'] // 100 + (log_data_1['FREQ'] % 100) / 100  


    ### LOG 3 ###
    #TEMPERATURAS
    log_data_3 = sample_data[sample_data[4] == "Log_3"]
    log_data_3 = log_data_3.iloc[:, 0:12]
    log_data_3.columns = ['MAC','FECHA','HORA','STATUS','LOG','T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']
    log_data_3 = log_data_3.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_3[['T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']] = log_data_3[['T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']].astype('int8')
    log_data_3['FECHA'] = pd.to_datetime(log_data_3['FECHA'])
    resultados = []
    i = 0

    # Itera a través de las columnas m1, m2, m3, m4, m5
    for columna in ['T_M1', 'T_M2', 'T_M3', 'T_M4',	'T_M5', 'T_M6',	'T_M7']:

        # Encuentra la temperatura máxima y su índice (hora) correspondiente
        max_temp = log_data_3[columna].max()
        hora_max_temp = log_data_3[log_data_3[columna] == max_temp]['HORA'].values[0]
        
        # Agrega los resultados a la lista
        lista = ['1', '2', '3', '4', '5', '6', '7']
        resultados.append((lista[i], max_temp, hora_max_temp))
        i = i + 1

    # Convierte la lista de resultados en un DataFrame
    resultados_df = pd.DataFrame(resultados, columns=['Modulo', 'Temperatura Max', 'HORA'])
    df_final = pd.merge(resultados_df, log_data_1, how='left')

    save = df_final

    # Convierte la lista de resultados en un DataFrame
    ttext = tk.Text(frame3, font=("Calibri", 12))
    ttext.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
    ttext.insert(tk.INSERT, df_final)


def getFailures():
    global save
    log_1 = sample_data[sample_data[4] == "Log_1"]
    df_fallas = log_1[[2,21]]
    df_fallas.columns = ['HORA','FALLO']
    df_fallas = df_fallas[df_fallas['FALLO'] != '0']
    df_fallas['HORA'] = pd.to_datetime(df_fallas['HORA'])
    df_fallas['diferencia_tiempo'] = df_fallas['HORA'].diff()
    intervalo_minimo = pd.Timedelta(minutes=3)
    fallas_unicas = df_fallas[df_fallas['diferencia_tiempo'] >= intervalo_minimo]
    fallas_unicas = fallas_unicas[['HORA', 'FALLO']] 
    fallas_unicas = fallas_unicas.sort_values('HORA', ascending=False).reset_index(drop=True)

    save = fallas_unicas

    ttext = tk.Text(frame3, font=("Calibri", 20))
    ttext.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
    ttext.insert(tk.INSERT, fallas_unicas)

def getWarnings():
    global save
    log_1 = sample_data[sample_data[4] == "Log_1"]
    df_advertencias = log_1[[2,22]]
    df_advertencias.columns = ['HORA','WARN']
    df_advertencias = df_advertencias[df_advertencias['WARN'] != '0']
    df_advertencias['HORA'] = pd.to_datetime(df_advertencias['HORA'])
    df_advertencias['diferencia_tiempo'] = df_advertencias['HORA'].diff()
    intervalo_minimo = pd.Timedelta(minutes=1)
    adv_unicas = df_advertencias[df_advertencias['diferencia_tiempo'] >= intervalo_minimo]
    adv_unicas = adv_unicas[['HORA', 'WARN']] 
    adv_unicas = adv_unicas.sort_values('HORA', ascending=False).reset_index(drop=True)
    save = adv_unicas

    ttext = tk.Text(frame3, font=("Calibri", 20))
    ttext.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
    ttext.insert(tk.INSERT, adv_unicas)

def getversions():
    ### Extract mac adress y software version ###
    version = sample_data.iloc[:1,5:21]
    version = version.values.tolist()
    #print(f"Software",sample_data.iat[0,4], version)
    ttext = tk.Text(frame3, font=("Calibri", 20))
    ttext.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
    ttext.insert(tk.INSERT, "La direccion mac es: "+sample_data.iat[0,0]) 
    ttext.insert(tk.INSERT, "\nSoftware "+sample_data.iat[0,4])
    ttext.insert(tk.INSERT, "\n")
    ttext.insert(tk.INSERT, version)

def plotTemp():
    ### LOG 3 ###
    #TEMPERATURAS
    log_data_3 = sample_data[sample_data[4] == "Log_3"]
    log_data_3 = log_data_3.iloc[:, 0:12]
    log_data_3.columns = ['MAC','FECHA','HORA','STATUS','LOG','T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']
    log_data_3 = log_data_3.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_3[['T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']] = log_data_3[['T_M1', 'T_M2','T_M3', 'T_M4', 'T_M5', 'T_M6', 'T_M7']].astype('int8')
    log_data_3['DateTime'] = pd.to_datetime(log_data_3['FECHA'] + ' ' + log_data_3['HORA'])

    plt.figure(figsize=(24, 14))
    plt.plot(log_data_3['DateTime'], log_data_3[['T_M1', 'T_M2', 'T_M3', 'T_M4','T_M5', 'T_M6',	'T_M7']], label=['T_M1', 'T_M2', 'T_M3', 'T_M4','T_M5', 'T_M6',	'T_M7'])
    plt.xticks(rotation=45)
    plt.legend()
    plt.show(); 

def plotPower():
    ### LOG 2 ###
    #POTENCIA MODULOS, ESTADO MODULOS   
    log_data_2 = sample_data[sample_data[4] == "Log_2"]
    log_data_2 = log_data_2.iloc[:,0:19]
    log_data_2.columns = ['MAC','FECHA','HORA','STATUS','LOG','P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7','E_M1', 
            'E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']
    log_data_2 = log_data_2.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_2[['P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7','E_M1', 
            'E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']] = log_data_2[['P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7','E_M1', 
            'E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']].astype('int16') 
    log_data_2['DateTime'] = pd.to_datetime(log_data_2['FECHA'] + ' ' + log_data_2['HORA'])

    plt.figure(figsize=(24, 14))
    plt.plot(log_data_2['DateTime'], log_data_2[['P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7']], label=['P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7'])
    plt.xticks(rotation=45)
    plt.legend()
    plt.show();

def plotModules():
    ### LOG 2 ###
    #POTENCIA MODULOS, ESTADO MODULOS   
    log_data_2 = sample_data[sample_data[4] == "Log_2"]
    log_data_2 = log_data_2.iloc[:,0:19]
    log_data_2.columns = ['MAC','FECHA','HORA','STATUS','LOG','P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7','E_M1', 
            'E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']
    log_data_2 = log_data_2.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_2[['P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7','E_M1', 
            'E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']] = log_data_2[['P_M1', 'P_M2','P_M3', 'P_M4', 'P_M5', 'P_M6', 'P_M7','E_M1', 
            'E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']].astype('int16') 
    log_data_2['DateTime'] = pd.to_datetime(log_data_2['FECHA'] + ' ' + log_data_2['HORA'])

    plt.figure(figsize=(24, 14))
    plt.plot(log_data_2['DateTime'], log_data_2[['E_M1','E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7']], label=['E_M1','E_M2','E_M3', 'E_M4', 'E_M5', 'E_M6', 'E_M7'])
    plt.xticks(rotation=45)
    plt.legend()
    plt.show();

def plotDC():
    log_data_1 = sample_data[sample_data[4] == "Log_1"]
    log_data_1 = log_data_1.iloc[:,0:17]
    log_data_1.columns = ['MAC','FECHA','HORA','STATUS','LOG','DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
                        'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']
    log_data_1 = log_data_1.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_1[['DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
            'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']] = log_data_1[['DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
            'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']].astype('int16') 
    log_data_1['FREQ'] = log_data_1['FREQ'] // 100 + (log_data_1['FREQ'] % 100) / 100
    log_data_1['DateTime'] = pd.to_datetime(log_data_1['FECHA'] + ' ' + log_data_1['HORA'])

    plt.figure(figsize=(24, 14))
    plt.plot(log_data_1['DateTime'], log_data_1[['DC_VOLTAGE_BUS', 'DC_VOLTAGE_PV','DC_INPUT_CURRENT']], label=['DC_VOLTAGE_BUS', 'DC_VOLTAGE_PV','DC_INPUT_CURRENT'])
    plt.xticks(rotation=45)
    plt.legend()
    plt.show(); 

def plotgrid():
    ## LOG 1 ###    
    log_data_1 = sample_data[sample_data[4] == "Log_1"]
    log_data_1 = log_data_1.iloc[:,0:17]
    log_data_1.columns = ['MAC','FECHA','HORA','STATUS','LOG','DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
                        'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']
    log_data_1 = log_data_1.drop(["MAC", "STATUS", "LOG"], axis=1)
    log_data_1[['DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
            'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']] = log_data_1[['DC_VOLTAGE_BUS','DC_VOLTAGE_PV','DC_INPUT_CURRENT','GRID_I1','GRID_I2','GRID_I3',
            'GRID_VRS','GRID_VST','GRID_VTR','P', 'Q','FREQ']].astype('int16') 
    log_data_1['FREQ'] = log_data_1['FREQ'] // 100 + (log_data_1['FREQ'] % 100) / 100
    log_data_1['DateTime'] = pd.to_datetime(log_data_1['FECHA'] + ' ' + log_data_1['HORA'])

    plt.figure(figsize=(24, 14))
    plt.plot(log_data_1['DateTime'], log_data_1[['GRID_I1','GRID_I2','GRID_I3','GRID_VRS','GRID_VST','GRID_VTR']], label=['GRID_I1','GRID_I2','GRID_I3','GRID_VRS','GRID_VST','GRID_VTR'])
    plt.xticks(rotation=45)
    plt.legend()
    plt.show();


### Crea ventana ###
#Titulo de la ventana
root.title("Script para SD")
#root.iconbitmap(r"Micro-SD-Card.ico") #Agregar icono a la ventana
#Crea la ventana principal
canvas = tk.Canvas(root, height=680, width=1250)
canvas.pack()

#Etiqueta Archivo cargado
label1 = tk.Label(root, text="Archivo cargado:")
label1.place(relx=-0.01, rely=0, relwidth=0.2, relheight=0.05, anchor="nw")
#Marco de carga de archivo #
frame1 = tk.Frame(root, bg="#001a57", bd=5)
frame1.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.05, anchor="nw")
#Boton para cargar#
loadCSV_B = tk.Button(frame1, text="Cargar archivo", font=20, command=getCSV)
loadCSV_B.place(relx=0.75, relheight=1, relwidth=0.25)

### Botones de acciones ###

#Seleccionar valores deseados#
label2 = tk.Label(root, text="Seleccionar acción a realizar:") 
label2.place(relx=0.013, rely=0.1, relwidth=0.2, relheight=0.05, anchor="nw")
# Marco de botones #
frame2 = tk.Frame(root, bg="#001a57", bd=2)
frame2.place(relx=0.05, rely=0.15, relwidth=0.90, relheight=0.1, anchor="nw")

# Boton para mostrar temperaturas max #
temps_b = tk.Button(frame2, text="Temperaturas max", font=15, command=getTempmax)  
temps_b.place(relx=0.0, relheight=0.5, relwidth=0.2)
# Boton para mostrar temps maximas e informacion #
tempsm_b = tk.Button(frame2, text="Temperaturas max info", font=15, command=Tempmaxinfo)
tempsm_b.place(relx=0.2, relheight=0.5, relwidth=0.2)
# Boton para mostrar fallos #
fallos_b = tk.Button(frame2, text="Fallas unicas", font=15, command=getFailures)
fallos_b.place(relx=0.4, relheight=0.5, relwidth=0.2)
# Boton para mostrar advertencias #
warnings_b = tk.Button(frame2, text="Mostrar Advertencias", font=15, command=getWarnings)
warnings_b.place(relx=0.6, relheight=0.5, relwidth=0.2)
# Boton para mostrar informacion del SW & HW #
info_b = tk.Button(frame2, text="MAC, DSP & FPGA Version", font=15, command=getversions)
info_b.place(relx=0.8, relheight=0.5, relwidth=0.2)

# Boton para graficar temperaturas de los módulos #
gtemps_b = tk.Button(frame2, text="Gráfica Temperaturas", font=15, command=plotTemp)
gtemps_b.place(relx=0.0, rely=0.5, relheight=0.5, relwidth=0.2)
# Boton para graficar potencia de modulos #
gpot_b = tk.Button(frame2, text="Gráfica Potencias", font=15, command=plotPower)
gpot_b.place(relx=0.2, rely=0.5, relheight=0.5, relwidth=0.2)
# Boton para graficar estados de modulos #
gedos_b = tk.Button(frame2, text="Gráfica Estados", font=15, command=plotModules)
gedos_b.place(relx=0.4, rely=0.5, relheight=0.5, relwidth=0.2)
# Boton para graficar valores de DC #
gdcs_b = tk.Button(frame2, text="Gráfica DC", font=15, command=plotDC)
gdcs_b.place(relx=0.6, rely=0.5, relheight=0.5, relwidth=0.2)
# Boton para graficar valores de AC  #
ggrids_b = tk.Button(frame2, text="Gráfica GRID", font=15, command=plotgrid)
ggrids_b.place(relx=0.8, rely=0.5, relheight=0.5, relwidth=0.2)


#Mostar resultados
label3 = tk.Label(root, text="Resultados")
label3.place(relx=-0.425, rely=0.25, relwidth=1, relheight=0.05, anchor="nw")

frame3 = tk.Frame(root,bg="#001a57") 
frame3.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.6, anchor="nw")
frame3 = tk.Frame(frame3,bg="white") 
frame3.place(relx=0.004, rely=0.01, relwidth=0.99, relheight=0.98, anchor="nw")

#Guardar resultados
label4 = tk.Label(root, text="Guardar como...")
label4.place(relx=0.09, rely=0.90, relwidth=0.8, relheight=0.04, anchor="n")

frame4 = tk.Frame(root, bg="#001a57", bd=3)
frame4.place(relx=0.05, rely=0.94, relwidth=0.9, relheight=0.05, anchor="nw")

loadCSV_B = tk.Button(frame4, text="Guardar archivo", font=20, command=exportCSV)
loadCSV_B.place(relx=0.75, relheight=1, relwidth=0.25)

root.mainloop()