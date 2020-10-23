from scipy import signal # para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


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


directorio = 'Data' # Indico directorio
fname = os.path.join(directorio,'OBS_SHN_SF-BA.csv') # Busco el archivo
df = pd.read_csv(fname, index_col=['Time'], parse_dates=True)

inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

# scipy.signal.detrend()

freq_sf, fft_sf = calcular_fft(alturas_sf)

plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# me quedo solo con el último pico
pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
print(pico_sf)
# es el pico a analizar, el de la onda de mareas
# marco ese pico con un circulito rojo
plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor = 'r')

ang_sf = np.angle(fft_sf)[pico_sf]
print(ang_sf)
# Obtenemos un valor cercano a pi/2. Recordemos que 2pi corresponde a un desfasaje de un ciclo completo de la curva. 
# Como nuestra curva de estudio tiene una frecuencia diaria ligeramente inferior a 2 (freq_sf[350]~1.93), 2pi corresponde 
# a 24/1.93 horas ~ 12.44 horas. Por lo tanto la fase obtenida con angSF[350] corresponde a un retardo de
print(ang_sf * 24 / (2 * np.pi * freq_sf[350]))

plt.show()