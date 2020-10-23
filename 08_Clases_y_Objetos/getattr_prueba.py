# 8.10
# https://github.com/python-unsam/UNSAM_2020c2_Python/blob/master/Notas/08_Clases_y_Objetos/03_Métodos_Especiales.md#ejercicio-810-ejemplo-de-getattr

import informe
from formato_tabla import crear_formateador, imprimir_tabla

camion = informe.leer_camion('Data/camion.csv')
formateador = crear_formateador('txt')
columnas = ['nombre', 'cajones']

imprimir_tabla(camion, columnas, formateador)