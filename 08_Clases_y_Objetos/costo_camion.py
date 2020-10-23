# ///---- tabla_informe.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import informe as informe
import lote
import sys

# ///---- Costo del camion ----///
def costo_camion(file_name):
    # Variables
    costo = 0
    rows = informe.leer_camion(file_name)

    # Imprimo datos y, a la vez, calculo precio de cajones
    for i, row in enumerate(rows, start=1):
        try:
            Ncajones = row.cajones
            Precio = row.precio
            costo += Ncajones * Precio
        except ValueError: # Si faltan datos, tirame un warning
            print(f'Fila {i}: No se puede interpretar: {row}')
    # Retorno con resultado
    return (costo)

# ///---- Main ----///
def main (argv):
    if len(sys.argv) != 2:
            raise SystemExit(f'Uso adecuado: {sys.argv[0]}' ' archivo_camion archivo_precios')
    duele = costo_camion('Data/camion.csv')
    print('\nTotal pagado por los cajones es: $', round(duele,2))

# ///---- Otros ----///
if __name__ == '__main__':
    main(sys.argv)