# tabla_informe.py

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


# Funcion hacer_informe
def hacer_informe(camion, precios):
    # Variables
    informe = []
    for itemA in camion:
        for itemB in precios:
            try:
                if itemA['nombre'] == itemB['producto']:
                    producto = itemA['nombre']
                    cantidad = int(itemA['cajones'])
                    precio = round(float(itemA['precio']),2)
                    cambio = round(float(itemB['billetin']) - precio, 2)
                    info = (producto, cantidad, precio, cambio)
                    informe.append(info)
            except KeyError:
                continue
    # Retorno con resultado
    return informe

# Carga de archivos en listas de diccionarios y tuplas
carga = leer_camion('Data/camion.csv')
chanta = leer_precios('Data/precios.csv')
informe = hacer_informe(carga, chanta)

# Generacion de tabla
head = ("Producto", "Cajones", "Precio", "Cambio")
print(f'{head[0]:^10s}|{head[1]:^10s}|{head[2]:^10s}|{head[3]:^10s}')
print("-------------------------------------------")
for info in informe:
    info = (info[0], info[1], '$'+str(info[2]), info[3])
    print(f'{info[0]:<10s}|{info[1]:^10d}|{info[2]:^10s}|{info[3]:^10.2f}')
    
    
    
    