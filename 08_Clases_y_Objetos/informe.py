# ///---- informe.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com


# ///---- Imports ----///
from fileparse import parse_csv
import sys
#import gzip # Descomentar para usar with gzip.open()
import lote
import formato_tabla


# ///---- Funcion leer_camion ----///
def leer_camion(file_name):
    #with gzip.open(file_name, 'rt') as file: # Descomentar este y comentar el de bajo para usar gzip
    with open(file_name, 'rt') as file:
        camion_dicts = parse_csv(file, types=[str,int,float])
        camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
        
        return (camion) # Retorno con resultado

# ///---- Funcion leer_precios ----///
def leer_precios(file_name):
    with open(file_name, 'rt') as file:
        venta = parse_csv(file ,types=[str,float], has_headers=False)
        header = ['producto', 'billetin'] # Asigno header
        precios = [dict(zip(header,tupa)) for tupa in venta]
        
        return (precios) # Retorno con resultado

# ///---- Funcion hacer_informe ----///
def hacer_informe(camion, precios):
    # Variables
    informe = []
    for itemA in camion:
        for itemB in precios:
            try:
                if itemA.nombre == itemB['producto']:
                    producto = itemA.nombre
                    cantidad = int(itemA.cajones)
                    precio = round(float(itemA.precio),2)
                    cambio = round(float(itemB['billetin']) - precio, 2)
                    info = (producto, cantidad, precio, cambio)
                    informe.append(info)
            except KeyError:
                continue
    
    return informe # Retorno con resultado

# ///---- Funcion imprimir_informe ----///
def imprimir_informe(informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    '''
    formateador.encabezado(["Producto", "Cajones", "Precio", "Cambio"]) # Cabecera de informe
    
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

    return # Retorno a main

# ///---- Funcion informe_camion ----///
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    carga = leer_camion(nombre_archivo_camion) # Leo datos del camion
    chanta = leer_precios(nombre_archivo_precios) # Leo los precios de venta
    
    informe = hacer_informe(carga, chanta) # Genero un informe

    formateador = formato_tabla.crear_formateador(fmt)

    imprimir_informe(informe, formateador) # Imprimo informe en pantalla

# ///---- Main ----///
def main(argv):
    if len(sys.argv) != 4:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]}' ' archivo_camion archivo_precios formato')
        # camion = "Data/camion.csv" # Descomenta estas 3 lineas si no te llevas bien con la consola
        # precios = "Data/precios.csv"
        # formato = "html"
    else:
        camion = sys.argv[1]
        precios = sys.argv[2]  
        formato = sys.argv[3]  

    informe_camion(camion, precios, formato)

# ///---- Otros ----///
if __name__ == '__main__':
    main(sys.argv)