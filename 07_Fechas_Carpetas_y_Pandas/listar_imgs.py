# ///---- listar_imgs.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import os
import pprint
import sys


# ///---- recorrido_img ----///
def recorrido_img(ruta):
    '''
    Recorro directorio y detecto imagenes *.png
    '''
    archivos = []   # Lista que va a contener ubicaciones de imagenes

    for root, dirs, files in os.walk(ruta): # Recorro ruta
        for name in files:
            archivo = os.path.join(root, name)
            if str(archivo)[-3:] == 'png':
                archivos.append(archivo)

    pprint.pprint(archivos)


# ///---- main ----///
def main(directorio):
    '''
    Funcion principal
    '''
    recorrido_img(directorio)


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
