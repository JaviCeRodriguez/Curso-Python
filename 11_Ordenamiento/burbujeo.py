# ///---- burbujeo.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

#! Funcionamiento:
#! El algoritmo compara dos elementos contiguos de la lista 
#! y, si el orden es adecuado, los deja como están, si no, los intercambia.

#///---- Orden por burbujeo ----///
def ord_burbujeo(lista):
    burb = 1
    aux = 0
    comparaciones = 0

    while burb == 1:
        burb = 0
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                burb = 1
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
            comparaciones += 1

    return comparaciones