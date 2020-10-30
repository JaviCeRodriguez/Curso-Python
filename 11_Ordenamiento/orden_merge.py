import random

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""

    lista_m=lista
    if len(lista_m) < 2:
        lista_nueva = lista_m
        comparaciones=0
        return lista_nueva, comparaciones
    else:
        medio = len(lista_m) // 2
        izq, comparaciones_izq = merge_sort(lista_m[:medio])
        der, comparaciones_der = merge_sort(lista_m[medio:])
        lista_nueva, comparaciones_merge = merge(izq, der)
        comparaciones=comparaciones_izq + comparaciones_der + comparaciones_merge

    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""

    i, j = 0, 0
    resultado = []
    compa=0
    while(i < len(lista1) and j < len(lista2)):
        compa+=1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado = resultado + lista1[i:]
    resultado = resultado + lista2[j:] 


    return resultado, compa