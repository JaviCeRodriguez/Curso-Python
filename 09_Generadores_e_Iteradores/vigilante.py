# ///---- vigilante.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import os
import time
import informe

# ///---- Vigilar ----///
def vigilar(file, encoding = 'UTF-8'):
    '''
    Recibe un archivo csv y lee en VIVO las lineas
    '''
    with open(file, 'r', encoding = 'UTF-8') as f:
        f.seek(0, os.SEEK_END)
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
        else:
            yield line

# ///---- __name__ ----///
if __name__ == '__main__':
    camion = informe.leer_camion ('Data/camion.csv')

    for line in vigilar('Data/mercadolog.csv', encoding = 'UTF-8'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')