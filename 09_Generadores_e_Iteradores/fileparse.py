# ///---- fileparse.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import csv
import gzip

# ///---- Funcion parse_csv ----///
# def parse_csv(nombre_archivo, select=None, types=None, has_headers=True, silence_errors = True):
def parse_csv(filas, select=None, types=None, has_headers=True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    # with open(nombre_archivo) as f:
    rows = csv.reader(filas)

    #! Si selecciono headers e indico a la vez que no tengo
    if select and not has_headers:
        raise RuntimeError("Dale man, dame encabezados si querés alguno")

    #! Con headers
    if has_headers:
        # Lee los encabezados
        headers = next(rows)
        # Selector de columnas
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []
        records = []
        for r, row in enumerate(rows):
            # Saltea filas sin datos
            if not row: 
                continue
            # Filtrado de filas (si el usuario quizo alguna)
            if indices:
                row = [row[index] for index in indices]
            # Si se indica tipos, aplico cambios
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as VE:
                if not silence_errors:
                    print(f'\tFila {r+1}: Datos invalidos! Datos de fila: {row}.\n\tMotivo: {VE}\n')
            # Diccionario
            record = dict(zip(headers, row))
            records.append(record)

    #! Sin header
    else:
        records = []
        for r, row in enumerate(rows):
            # Saltea filas sin datos
            # if not row:
            #     continue
            # Si se indica tipos, aplico cambios
            try:
                if types:
                    row = tuple([func(val) for func, val in zip(types, row)])
            except ValueError as VE:
                if not silence_errors:
                    print(f'\tFila {r+1}: Datos invalidos! Datos de fila: {row}.\n\tMotivo: {VE}\n')
            # Lista de tuplas
            records.append(row)

    return records

# ///---- Main ----///
with gzip.open('Data/camion.csv.gz', 'rt') as file:
    camion = parse_csv(file, types = [str,int,float], silence_errors = True)
# print(camion)