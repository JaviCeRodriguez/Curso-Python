# ///---- mareas_a_mano.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# En este tuve problemas para obtener los datos del puerto de Zarate
# Entrego lo que pude hacer

# ///---- Imports ----///
from scipy import signal # para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


# ///---- calcular_fft ----///
def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran


# ///---- ang_frec ----///
def ang_frec(alturas):
    freq, fft = calcular_fft(alturas)
    plt.plot(freq, np.abs(fft))
    plt.xlabel("Frecuencia")
    plt.ylabel("Potencia (energía)")
    plt.xlim(0,4)
    plt.ylim(0,20)
    # me quedo solo con el último pico
    pico = signal.find_peaks(np.abs(fft), prominence = 8)[0][-1]
    #se grafican los picos como circulitos rojos
    plt.scatter(freq[pico], np.abs(fft)[pico], facecolor='r')

    ang = np.angle(fft)[pico]
    frec = freq[pico]

    return (ang, frec)


# ///---- main ----///
def main(archivo1, archivo2):
    '''
    Funcion principal
    '''
    directorio = 'Data' # Indico directorio
    fname1 = os.path.join(directorio,archivo1) # Busco el archivo1
    fname2 = os.path.join(directorio,archivo2) # Busco el archivo2

    df_basf = pd.read_csv(fname1, index_col=['Time'], parse_dates=True)
    df_za = pd.read_csv(fname2, index_col=['Time'], parse_dates=True)

    inicio = '2014-01' # Inicio de analisis
    fin = '2014-06' # Fin de analisis

    # alturas_sf = df_basf[inicio:fin]['H_SF'].to_numpy()
    alturas_ba = df_basf[inicio:fin]['H_BA'].to_numpy()
    alturas_za = df_za[inicio:fin]['H_Zarate'].to_numpy()

    plt.subplot(1,2,1)
    (ang_ba, frec_ba) = ang_frec(alturas_ba)
    plt.subplot(1,2,2)
    (ang_za, frec_za) = ang_frec(alturas_za)

    ang2h = 24 / (2*np.pi*frec_ba)
    print("El desfasaje de las ondas de Zarate es:", (ang_ba - ang_za) * ang2h)

    plt.show()


# ///---- sys ----///
if __name__ == '__main__':
    try:
        if len(sys.argv) == 3: # Si paso dos argumentos, lo guardo
            archivo1 = sys.argv[1]
            archivo2 = sys.argv[2]
        else: # Si no, entro por default al asignado
            archivo1 = 'OBS_SHN_SF-BA.csv' 
            archivo2 = 'OBS_Zarate_2013A.csv'
    except FileNotFoundError:
        print(f'No se encuentran archivos!')
    main(archivo1, archivo2)