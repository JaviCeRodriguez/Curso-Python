# ///---- plot_bbin_vs_bsec.py ----///
# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import random
import matplotlib.pyplot as plt
import numpy as np

# ///---- Genero lista ----///
#! Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

# ///---- Genero elemento ----///
#! Devuelve un elemento aleatorio en el mismo rango de valores
def generar_elemento(m):
    return random.randint(0, m-1)

# ///---- Busqueda secuencial ----///
#! Realiza una búsqueda secuencial de un elemento en una lista. Devuelve 
#! la posición del elemento si lo encuentra y -1 si no lo encuentra.
#! Además, devuelve cuántas comparaciones (z == x) hace la función
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

# ///---- Cantidad de comparaciones promedio (secuencial)----///
#! Da la cantidad de comparaciones promedio en k experimentos elementales.
def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

# ///---- Busqueda binaria ----////
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comps = 0
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
        comps += 1
    return (pos, comps)

# ///---- Cantidad de comparaciones promedio (binario) ----///
def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

# ///---- Principal ----///
m = 10000 # Rango de random.sample
n = 100 # Muestra
k = 1000 # Experimentos elementales
# lista = generar_lista(n, m)

# # acá comienza el experimento
# x = generar_elemento(m)
# comps = busqueda_secuencial_(lista, x)[1] #Posicion 0, Comparaciones 1
largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_bin = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_sec = np.zeros(256) # y aca tambien.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio_sec,label = 'Búsqueda Secuencial')
plt.plot(largos,comps_promedio_bin,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
# plt.xlim([0, 250])
# plt.ylim([1, 8])
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()

#! ¿Qué observas en estos gráficos? ¿Qué podés decir sobre la complejidad de cada algoritmo? ¿Son similares?
#* Se nota a simple vista que la busqueda secuencial demanda una gran cantidad de comparaciones, mientras que
#*la busqueda binaria es mas eficaz casi sin importar el largo de la lista.
#* La complejidad de cada algoritmo (para mi), son similares. Pero una demanda mucho mas tiempo que la otra.