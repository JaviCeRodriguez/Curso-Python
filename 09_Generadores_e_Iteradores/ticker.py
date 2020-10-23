# ///---- ticker.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
from vigilante import vigilar
import csv
import informe
import formato_tabla

# ///---- ticker ----///
def ticker(camion_file, log_file, fmt):
    '''
    Imprime por pantalla en el formato deseado
    '''
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file), types = [str, str, str])
    filas = filtrar_datos (filas, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    while True:
        for fila in filas:
           formateador.fila(fila.values())

# ///---- filtrar_datos ----///
def filtrar_datos(filas, nombres):
    '''
    Filtrador por nombre
    '''
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

# ///---- cambiar_tipo ----///
def cambiar_tipo(rows, types):
    '''
    Cambia el tipo de cada elemento de fila
    '''
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

# ///---- hace_dicts ----///
def hace_dicts(rows, headers):
    '''
    Crea diccionarios
    '''
    for row in rows:
        yield dict(zip(headers, row))

# ///---- elegir_columnas ----///
def elegir_columnas(rows, indices):
    '''
    Elije columnas de un archivo
    '''
    for row in rows:
        yield [row[index] for index in indices]


# ///---- parsear_datos ----///
def parsear_datos(lines, types = [str, float, float]):
    '''
    Parseo de lineas
    '''
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, types) # [str, float, float]
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

# ///---- __name__ ----///
if __name__ == '__main__':
    #! Para probar pasear_datos
    # lines = vigilar('Data/mercadolog.csv')
    # rows = parsear_datos(lines)
    # for row in rows:
    #     print(row)

    #! Para probar filtrar_datos
    # camion = informe.leer_camion('Data/camion.csv')
    # filas = parsear_datos(vigilar('Data/mercadolog.csv'))
    # filas = filtrar_datos (filas, camion)
    # for fila in filas:
    #     print(fila)

    #! Para probar ticker
    # camion = 'Data/camion.csv'
    # filas = 'Data/mercadolog.csv'
    # formato = 'html'
    # ticker(camion, filas, formato)