import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys


def boxplot_arboles(df_sel, cols): # 7.8
    '''
    Diagrama en caja de arboles previamente seleccionados
    '''
    df_sel.boxplot('altura_arbol', by = 'nombre_cientifico')
    plt.figure(1)

    sns.pairplot(data = df_sel[cols], hue = 'nombre_cientifico')
    plt.show()
    # ancho_acera no aparece en el grafico porque tiene valores NaN, creo


def lectura_y_seleccion(df, cols): # 7.7
    '''
    Leo las columnas del archivo
    '''
    df_lineal = df[cols]
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    print(df_lineal_seleccion)

    return(df_lineal_seleccion)


def main(archivo):
    '''
    Funcion principal
    '''
    directorio = 'Data' # Indico directorio
    fname = os.path.join(directorio,archivo) # Busco el archivo
    df = pd.read_csv(fname)
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    
    df_selected = lectura_y_seleccion(df, cols_sel) # Imprimo diez especies mas frecuentes
    boxplot_arboles(df_selected, cols_sel) # Realizo Diagrama en Caja


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2: # Si paso dos argumentos, lo guardo
            archivo = sys.argv[1]
        else:
            archivo = 'arbolado-publico-lineal-2017-2018.csv' # Si no, entro por default al asignado
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv[1]}')
    main(archivo)