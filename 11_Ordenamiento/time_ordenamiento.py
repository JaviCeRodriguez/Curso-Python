# ///---- time_ordenamiento.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com
# Parte del código es de Hernan Diez

#///---- Imports ----///
import time
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt

#///---- Generacion de listas ----///
def generar_listas(N):
    Lista=[]
    for i in range(1,N):
        lista = np.random.randint (1,1000,i)
        Lista.append(lista)
    return Lista

#!------------------------------------------------------------------------------

#///---- Ordenamiento por burbujeo ----///
def ord_burbujeo(lista):
        n = len (lista) - 1
        while(n > 0):  # 
            for i,val in enumerate(lista):
                if i+1 != len (lista):  # le esquivo el error 
                    if val > lista[i+1]:
                        aux = lista[i+1]
                        lista[i+1] = val
                        lista [i] = aux
                        
            n -= 1
           
        return lista

#!------------------------------------------------------------------------------

#///---- Ordenamiento por seleccion ----///
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        

        # reducir el segmento en 1
        n = n - 1

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#!------------------------------------------------------------------------------

#///---- Ordenamiento por insercion ----///
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        
def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#!------------------------------------------------------------------------------ 

#///---- Ordenamiento por Merge ----///
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
        Pre: lista1 y lista2 deben estar ordenadas.
        Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado = resultado + lista1[i:]
    resultado = resultado + lista2[j:] 

    return resultado

#!------------------------------------------------------------------------------ 

#///---- Comparaciones por tiempo ----///
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion_1 = []
    tiempos_seleccion_2 = []
    tiempos_seleccion_3 = []
    tiempos_seleccion_4 = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion_1 = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_seleccion_2 = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempo_seleccion_3 = tt.timeit('ord_burbujeo(lista)', number = num, globals = globals())
        tiempo_seleccion_4 = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion_1.append(tiempo_seleccion_1)
        tiempos_seleccion_2.append(tiempo_seleccion_2)
        tiempos_seleccion_3.append(tiempo_seleccion_3)
        tiempos_seleccion_4.append(tiempo_seleccion_4)
        
    # paso los tiempos a arrays
    tiempos_seleccion_S = np.array(tiempos_seleccion_1)
    tiempos_seleccion_I = np.array(tiempos_seleccion_2)
    tiempos_seleccion_B = np.array(tiempos_seleccion_3)
    tiempos_seleccion_M = np.array(tiempos_seleccion_4)
    
    return tiempos_seleccion_S, tiempos_seleccion_I, tiempos_seleccion_B, tiempos_seleccion_M

#!------------------------------------------------------------------------------ 

#///---- Main ----///
lista = generar_listas(256)
(Seleccion,Insercion,Burbuja,Merge) = experimento_timeit_seleccion(lista, 256)

plt.plot(Seleccion, color="red", linewidth=2.0,label="Selección")
plt.plot(Burbuja, color="blue", linewidth=1.0,label="Burbuja")
plt.plot(Insercion, color="green", linewidth=1.0, label="Inserción")
plt.plot(Merge, color="black", linewidth=1.0, label="Merge")

plt.xlabel("Largo de la lista")
plt.ylabel("Tiempo de las comparaciones")
plt.title("Comparaciones de Ordenamiento")
legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')

plt.show()








