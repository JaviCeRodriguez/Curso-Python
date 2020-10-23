# ///---- bbin_rec.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

def bbinaria_rec(lista, e):
    '''
    Realizo busqueda binaria de un valor 'e' dentro de una lista dada
    '''
    if len(lista) == 0: # Caso base: lista vacia
        res = False
    elif len(lista) == 1: # Caso base: lista con un elemento e igual al buscado
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if e in lista[:medio]:
            return bbinaria_rec(lista[:medio], e)
        else:
            return bbinaria_rec(lista[medio:], e)
    return res

lista = [2, 2, 4, 1, 7, 3, 8, 3]
e = 4
print(bbinaria_rec(lista, e))