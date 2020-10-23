# ///---- fileparse.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import csv

# ///---- Funcion parse_csv ----///
def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

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
            for row in rows:
                # Saltea filas sin datos
                if not row: 
                    continue
                # Filtrado de filas (si el usuario quizo alguna)
                if indices:
                    row = [row[index] for index in indices]
                # Si se indica tipos, aplico cambios
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                # Diccionario
                record = dict(zip(headers, row))
                records.append(record)

        #! Sin header
        else:
            records = []
            for row in rows:
                # Saltea filas sin datos
                if not row:
                    continue
                # Si se indica tipos, aplico cambios
                if types:
                    row = tuple([func(val) for func, val in zip(types, row)])
                # Lista de tuplas
                records.append(row)

    return records

# ///---- Main ----///
camion = parse_csv('Data/camion.csv')
#print(camion)