 camion = informe.leer_camion('Data/camion.csv')
    filas = parsear_datos(vigilar('Data/mercadolog.csv'))
    filas = filtrar_datos (filas, camion)
    for fila in filas:
        print(fila)