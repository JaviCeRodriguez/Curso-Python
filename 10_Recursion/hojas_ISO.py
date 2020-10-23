# ///---- hojas_ISO.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

def A(N):
    '''
    Dado un valor N >= 0, obtengo ancho y largo de la hoja
    '''
    ancho = 841
    largo = 1189

    if N > 10: # Caso base: N mayor a norma establecida
        return f'Tamaño mínimo: A10'
    elif N == 0: # Caso base: N == 0
        return (ancho, largo)
    else:
        (ancho, largo) = A(N-1)
        if ancho > largo:
            ancho //= 2
        else:
            largo //= 2
        return (ancho, largo)
    
for j in range(11):
    (ancho, largo) = A(j)
    print(f'Hoja A{j} => Ancho: {ancho} y Largo: {largo}')
