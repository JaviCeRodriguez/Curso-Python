# ///---- fileparse.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Insertar elemento a lista ----///
def insertar(lista, x):
    lista.append(x)
    lista = sorted(lista)
    return(lista)

# ///---- Busqueda binaria ----///
def donde_insertar(lista, x, verbose = False):
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
    
    if pos != -1:
        print("Encontrado!")
        return pos
    else:
        print("No encontrado!")
        if lista[medio] > x:
            print("Nueva lista: ", insertar(lista, x))
            return medio
        else: # lista[medio] < x
            print("Nueva lista: ", insertar(lista, x))
            return medio+1

# ///---- Main ----///
listaNO = [] # Variable para lista no ordenada
listaO = [] # Variable para lista ordenada
print("Posicion de ubicacion: ", donde_insertar([0, 2, 4, 6, 9, 23, 55, 56], 3, verbose=True))
#! Descomentar las líneas de abajo y comentar el print de arriba para poner listas manualmente
# N = int(input('Cuantos elementos quiere ingresar en la lista?: ')) # Numero de elementos en lista
# for i in range(0,N):
#     listaNO.append(input('Ingrese valor: ')) # Ingreso elementos
# listaO = sorted(listaNO) # Ordeno lista
# elemento = input('Ingrese valor a buscar: ') # Pregunto por valor a buscar
# print(donde_insertar(listaO, elemento, verbose=True))