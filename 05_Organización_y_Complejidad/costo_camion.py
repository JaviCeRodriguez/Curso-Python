# costo_camion.py
# Abre archivo camion.csv ('Data/camion.csv')
#lee las lineas y calcula el precio pagado por los
#cajones cargados en el camion

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# Importo biblioteca
#import csv
import informe_funciones as informe

# Funcion costo_camion
def costo_camion(file_name):
    # Variables
    costo = 0
    
    rows = informe.leer_camion(file_name)

    #! Comentado para utilizar import informe_funciones
    # # Abro archivo camion.csv
    # #file = open(file_name, 'rt')
    # file = open(file_name)
    # rows = csv.reader(file)
    
    # Salteo cabecera y la guardo
    #header = next(rows)
    
    # Imprimo datos y, a la vez, calculo precio de cajones
    for i, row in enumerate(rows, start=1):
        try: # Si no hay datos faltantes, hace la cuenta
            # record = dict(zip(header,row))
            # Ncajones = int(record['cajones'])
            # Precio = float(record['precio'])
            Ncajones = row['cajones']
            Precio = row['precio']
            costo += Ncajones * Precio
        except ValueError: # Si faltan datos, tirame un warning
            print(f'Fila {i}: No se puede interpretar: {row}')
    # # Cierro archivo camion.csv
    # file.close()
    
    # Retorno con resultado
    return (costo)

# Resultado
duele = costo_camion('Data/camion.csv')
print('\nTotal pagado por los cajones es: $', round(duele,2))