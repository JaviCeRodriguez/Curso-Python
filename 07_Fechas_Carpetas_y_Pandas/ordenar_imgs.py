# ///---- ordenar_img.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import os
import datetime
import pprint
import sys
import shutil
import numpy as np


# ///---- move_imgs ----///
def move_imgs():
    # esta funcion la usaria para mover las imagenes, pero no logre entender
    #como es el procedimiento (me falto tiempo igualmente, mi culpa)
    pass

# ///---- walk_rename ----///
def walk_y_rename(ruta, destino):
    '''
    Recorro directorio y detecto imagenes *.png
    Luego modifico fecha y las renombro
    '''
    for root, dirs, files in os.walk(os.path.join(ruta,'ordenar')): # Recorro ruta
        for name in files:
            archivo = os.path.join(root, name)
            if name[-3:] == 'png':
                # print(name)
                fecha = archivo[-12:-4]
                fecha_mod = datetime.datetime(year = int(fecha[0:4]), month = int(fecha[4:6]), day = int(fecha[6:8]))
                ts_mod = fecha_mod.timestamp()
                direccion = os.path.join(root, name)
                os.utime(direccion, (ts_mod, ts_mod))
                os.rename(direccion, direccion[:-13] + '.png')
            # elif name[-3:] == 'png' and name[-13] != '_':
            #     print("\nNo se puede volver a procesar imagenes!\nYa fueron modificadas o no tienen formato 'name_AAAAMMDD.png'\n")
            #     break
    return os.listdir(ruta)


# ///---- crear_carpeta ----///
def crear_carpeta(ruta, carpeta):
    '''
    Creo subdirectorio dentro de la ruta especificada
    '''
    try:
        os.mkdir(os.path.join(ruta, carpeta))
        print(f"Mostrando directorio {ruta}\n")
    except FileExistsError:
        print(f"El subdirectorio {carpeta} ya existe!\n")


# ///---- main ----///
def main(directorio):
    '''
    Funcion principal
    '''
    carpeta_nueva = 'imgs_procesadas'

    crear_carpeta(directorio, carpeta_nueva)
    walk_y_rename(directorio, carpeta_nueva)


# ///---- sys ----///
if __name__ == '__main__':
    try:
        if len(sys.argv) == 2: # Si paso dos argumentos, lo guardo
            ruta = sys.argv[1]
        else:
            ruta = '.\Data' # Si no, entro por default al asignado
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv[1]}')
    main(ruta)
