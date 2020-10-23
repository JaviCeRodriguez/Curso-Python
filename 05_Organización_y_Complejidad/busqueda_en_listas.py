# busqueda_en_listas.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Busco elemento en lista ----///
def buscar_u_elemento(lista, elem): # Ejercicio 3.6
    pos = -1 # Considero inicialmente que elem no esta en lista
    for i, l in enumerate(lista):
        if l == elem: # Si encuentro elem en lista, obtengo pos y salgo
            pos = i
            break
    return pos

# ///---- Busco elemento en lista ordenada (5.10)----///
def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    lordenada = sorted(lista)
    i = 0     
    for z in lordenada:  # recorremos los elementos de la lista
        if z > e: # Si z es mayor a e, 
            break
        else:
            pos = i
        i += 1       
    return pos

# ///---- Busco veces que aparece elemento en lista ----///
def buscar_n_elemento(lista, elem): # Ejercicio 3.6
    v = 0 # Variable de veces inicializo en 0
    for l in lista:
        if l == elem:
            v += 1
    return v

# ///---- Busco maximo en lista (considero que tengo lista de int) ----///
def maximo(lista): # Ejercicio 3.7
    maxi = 0 # Variable con valor inicial
    for i, l in enumerate(lista):
        if i == 0: # Tomo el primer valor de la lista como referencia
            maxi = int(l)
        if int(l) > maxi:
            maxi = int(l)
    return maxi

# ///---- Busco minimo en lista (considero que tengo lista de int) ----///
def minimo(lista): # Ejercicio 3.7
    mini = 0 # Variable con valor inicial
    for i, l in enumerate(lista):
        if i == 0: # Tomo el primer valor de la lista como referencia
            mini = int(l)
        if int(l) < mini:
            mini = int(l)
    return mini

# ///---- Variables ----///
lisssta = list()

# ///---- Codigo principal ----///
N = int(input('Cuantos elementos quiere ingresar en la lista?: ')) # Numero de elementos en lista
for i in range(0,N):
    lisssta.append(input('Ingrese valor: ')) # Ingreso elementos

elemento = input('Ingrese valor a buscar: ') # Pregunto por valor a buscar

pos = buscar_u_elemento(lisssta, elemento) # Busco elemento
if pos != -1: # Si se encontro uno o mas elementos, puedo seguir con el resto del programa
    veces = buscar_n_elemento(lisssta, elemento) # Averguo las veces que aparece
    print(f'{elemento} aparece en la posicion {pos} (primera detectada) y aparece {veces} veces')
    maximoInt = maximo(lisssta) # Obtengo maximo entero
    minimoInt = minimo(lisssta) # Obtengo minimo entero
    print(f'Maximo valor de la lista es {maximoInt}, y el minimo es {minimoInt}')
else:
    print('No se encontraron datos coincidentes') # Si no encuentro elementos, termina programa