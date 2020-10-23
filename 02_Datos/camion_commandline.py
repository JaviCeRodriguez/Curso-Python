# costo_camion.py
# Abre archivo camion.csv ('Data/camion.csv')
#lee las lineas y calcula el precio pagado por los
#cajones cargados en el camion

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# Importo bibliotecas
import csv
import sys

# Funcion costo_camion
def costo_camion(file_name):
    # Variables
    costo = 0
    
    # Abro archivo camion.csv
    #file = open(file_name, 'rt')
    file = open(file_name)
    rows = csv.reader(file)
    
    # Imprimo cabecera para formar una "tabla"
    head = next(rows) # Guardo cabecera en head
    print('{0:10s} {1:10s} {2:10s}'.format(head[0], head[1], head[2]))
    
    # Imprimo datos y, a la vez, calculo precio de cajones
    for line in file:
        row = line.split(',')
        print('{0:10s} {1:10s} {2:10s}'.format(row[0], row[1], row[2]))
        try: # Si no hay datos faltantes, hace la cuenta
            costo = costo + (float(row[1]) * float(row[2]))
        except ValueError: # Si faltan datos, tirame un warning
            print('Error detectado en una de las celdas de la fila de', row[0])
    # Cierro archivo camion.csv
    file.close()
    
    # Retorno con resultado
    return (costo)

# Inclusion de archivo a leer
if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'Data/missing.csv'

# Resultado
duele = costo_camion(file_name)
print('\nTotal pagado por los cajones es:', round(duele,2))