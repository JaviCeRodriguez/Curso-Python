# ///---- mareas_a_mano.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


# ///---- shift_serie ----///
def shift_serie(df_mareas):
    '''
    Desplazamiento de Series
    '''
    dh = df_mareas['12-25-2014':].copy()

    delta_t = 2 # tiempo que tarda la marea entre ambos puertos
    delta_h = 3 # diferencia de los ceros de escala entre ambos puertos
    pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()


# ///---- lectura_plots ----///
def lectura_plots(df_mareas):
    '''
    Realiza lectura de prueba para imprimir y hace 2 plots
    en distintos intervalos de tiempo
    '''
    print(df_mareas['1-18-2014 9:00':'1-18-2014 18:00'])

    df_mareas['10-15-2014':'12-15-2014'].plot() # Ondas de marea en el RdlP
    df_mareas['12-25-2014':].plot() # Vientos y ondas de tormenta en el RdlP


# ///---- main ----///
def main(archivo):
    '''
    Funcion principal
    '''
    directorio = 'Data' # Indico directorio
    fname = os.path.join(directorio,archivo) # Busco el archivo
    df = pd.read_csv(fname, index_col=['Time'], parse_dates=True)
    
    lectura_plots(df)
    shift_serie(df)

    plt.show()


# ///---- sys ----///
if __name__ == '__main__':
    try:
        if len(sys.argv) == 2: # Si paso dos argumentos, lo guardo
            archivo = sys.argv[1]
        else:
            archivo = 'OBS_SHN_SF-BA.csv' # Si no, entro por default al asignado
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv[1]}')
    main(archivo)