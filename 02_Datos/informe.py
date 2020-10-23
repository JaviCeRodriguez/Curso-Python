# informe.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# Importo biblioteca
import csv

# Variables
total = 0
venta = 0

# Funcion leer_camion
def leer_camion(file_name):
    # Variables
    camion = list()
    
    # Abro archivo camion.csv
    file = open(file_name)
    rows = csv.reader(file)
    
    header = next(rows) # Guardo cabezera y voy a la siguiente linea
    
    # Leo resto de lineas
    for line in rows:
        lote = dict(zip(header, line))
        camion.append(lote)
        
    # Cierro archivo camion.csv
    file.close()
    
    # Retorno con resultado
    return (camion)

# Funcion leer_precios
def leer_precios(file_name):
    # Variables
    venta = list()

    # Abro archivo precios.csv
    file = open(file_name)
    rows = csv.reader(file)
    
    # Asigno header
    header = ['producto', 'billetin']
    
    # Leo contenido del archivo
    for line in rows:
        try:
            price = dict(zip(header, line))
            venta.append(price)
        except IndexError:
            print('Fin de analisis de datos\n\n')
    
    # Cierro archivo precios.csv
    file.close()
    
    # Retorno con resultado
    return (venta)

# Carga de archivos en listas de diccionarios
carga = leer_camion('Data/camion.csv')
chanta = leer_precios('Data/precios.csv')

# Balance
for itemA in carga:
    total += int(itemA['cajones']) * float(itemA['precio'])
    for itemB in chanta:
        try:
            if itemB['producto'] == itemA['nombre']:
                venta += int(itemA['cajones']) * float(itemB['billetin'])
        except KeyError:
            print('Error de lectura')


# Pantalla
print('Total pagado en descarga del camion: $', total)
print('Coste del camion: $', round(venta-total, 2))
print('Ganancia del vendedor: $', venta)

