# ///---- tabla_informe.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import informe as informe
import lote
import sys

# ///---- Costo del camion ----///
def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total()

# ///---- Main ----///
def main (argv):
    if len(sys.argv) != 2:
            raise SystemExit(f'Uso adecuado: {sys.argv[0]}' ' archivo_camion archivo_precios')
    duele = costo_camion('Data/camion.csv')
    print('\nTotal pagado por los cajones es: $', round(duele,2))

# ///---- Otros ----///
if __name__ == '__main__':
    main(sys.argv)