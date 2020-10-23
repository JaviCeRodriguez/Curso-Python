def donde_insertar(lista,x):
    pos=-1 #Inicializo en -1 para que no influya
    if x in lista: #Si esta en la lista busco su posicion
        for i in range(len(lista)):
            if x == lista[i]:
                #print(f'i = {i} y el valor de lista[i] es {lista[i]} y de lista[i+1] es {lista[i+1]}')
                pos = i
    else:  #Si no esta me fijo donde deberia estar
        for i in range(len(lista)):
            '''Como tomo la precondicion de que la lista esta ordenada, si tomo
            que x sea mayor al valor en i y menor al valor en i+1, puedo encontrar
            la posicion donde deberia ubicarse'''
            if i+1 != len(lista):
                #print('Entro al True')
                if x >= lista[i] and x <= lista[i+1]:
                    #print(f'i = {i} y el valor de lista[i] es {lista[i]} y de lista[i+1] es {lista[i+1]}')
                    pos = i+1
                    break
            else:
                #print('Entro al False')
                pos = len(lista)
                
    return pos

#Recibe una lista ordenada y una posicion e inserta el valor faltante en esa posicion
def insertar(lista,posicion,valor):
    #print('Entro a funcion insertar')
    listaDevolver = lista.copy()
    #print(f'El valor de posicion es {posicion}')
    listaDevolver.append(valor)
    listaDevolver = sorted(listaDevolver)
    return listaDevolver

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos ==-1:
        pos_insertar = donde_insertar(lista, x)
        #print(f'El valor de la posicion a insertar es {pos_insertar}')
        lista = insertar(lista,pos_insertar,x)
        return lista,pos_insertar
        
    return lista,pos



x=7
listaPedida = [0,2,4,6]
lista,pos = busqueda_binaria(listaPedida, x)
if len(lista) == len(listaPedida):
    print(f'La lista contenia al valor pedido, en este caso: {x} y se encuentra en la posicion {pos} y la lista se mantiene igual {lista}')
else:
    print(f'La lista no contenia al valor pedido, en este caso: {x} y se encuentra en la posicion {pos} y la lista cambia y pasa a ser: {lista}')