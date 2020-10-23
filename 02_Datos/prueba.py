import csv
from pprint import pprint  #para una impresion mas ordenada
from collections import Counter

def leer_parque(nombre_archivo, parque):  #'parque' es el grupo especificado
    'Retorna una lista de diccionarios de cada arbol dentro del "parque" especificado'
    arboles = [] #lista de diccionarios
    arbol = {}  #diccionario vacio
    f = open(nombre_archivo, 'rt', encoding='utf8')
    filas = csv.reader(f)
    encabezados = next(filas)
    for fila in filas:
        arbol = dict(zip(encabezados, fila))
        if arbol['espacio_ve'] == parque:
            arboles.append(arbol)  
    f.close()
    return arboles

def especies(lista_arboles):  #recibe una lista de dicc
    'Retorna un conjunto con los nombres de las especies dentro de "lista_arboles"'
    especies = set([]) #conjunto vacio
    for arbol in arboles:
        especies.add(arbol['nombre_com'])
    return especies

def contar_ejemplares(lista_arboles):
    'Retorna la cantidad de arboles de cada especie que existe dentro de "lista_arboles"'
    n_ejem = Counter()
    for arbol in arboles:
        n_ejem[arbol['nombre_com']] += 1
    n_especies = dict(n_ejem)
    return n_especies, n_ejem  #retorno el diccionario y el contador

def obtener_alturas(lista_arboles, especie):
    'Retorna una lista con la altura de cada ejemplar de "especie" dentro de "lista_arboles"'
    alturas = []  #defino lista vacia
    try:
        for arbol in lista_arboles:
            if arbol['nombre_com'] == especie:
                alturas.append(float(arbol['altura_tot']))
    except:
        print(f'No existen {especie} en la lista')
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    'Retorna una lista con las inclinaciones de los ejemplares de "especie" en "lista_arboles"'
    inclinaciones = [] #lista vacia
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    'Retorna la especie y la inclinacion del ejemplar mas inclinado'
    esp = list(especies(lista_arboles)) #convierto en lista el conjunto
    max_inclinacion = []  #maximo entre todas las especies
    max_inc_esp = [] #maxima inclinacion dentro de una especie
    for i in range(len(esp)):
        inclinaciones = obtener_inclinaciones(lista_arboles, esp[i])
        max_inc_esp.append([int(max(inclinaciones)), esp[i]])  #guarda una lista con
                                                               #un valor max por cada
                                                               #especie, de todas las espcs.

    max_inclinacion = max(max_inc_esp)
    return max_inclinacion  #solo retornara una especie max, segun (valor, orden alfab)-Corregir falencia

def especie_promerdio_mas_inclinada(lista_arboles):
    'Retorna la especie de mayor inclinacion promedio, y el promedio'
    esp = list(especies(lista_arboles)) #convierto en lista el conjunto
    max_inclinacion = []
    max_prom_esp = []
    for i in range(len(esp)):
        inclinaciones = obtener_inclinaciones(lista_arboles, esp[i])
        prom = float(sum(inclinaciones)/len(inclinaciones))
        max_prom_esp.append([round(prom,2), esp[i]])  #lista con
                                                      #un valor promedio por cada
                                                      #especie, de todas las espcs.

    max_inclinacion = max(max_prom_esp)
    return max_inclinacion


######### IMPLEMENTACION DE FUNCIONES ################################

         
parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO', 'INDOAMERICANO']
for parque in parques:
    try:    
        arboles = leer_parque('Data/arbolado-en-espacios-verdes.csv',parque)
        espec = especies(arboles)
        especie = 'Jacarandá'  #especie usada como prueba
        alturas = obtener_alturas(arboles, especie)
        prop = (round(max(alturas),2), round(sum(alturas)/len(alturas),2))
        n_especies, n_ejem = contar_ejemplares(arboles)
        inclinaciones = obtener_inclinaciones(arboles, especie)
        max_inclinacion = especimen_mas_inclinado(arboles)
        max_prom_inc = especie_promerdio_mas_inclinada(arboles)

        print(f'\n\n\nLa cantidad de arboles en el parque {parque} es de {len(arboles)}')  #ejer 2.22
        print('\n\n\n')

        print(f'Las especies existentes en el parque {parque} son:')  #ejer 2.23
        pprint(espec)     #ejer 2.23
        print('\n\n\n')

        print(f'Las cinco especies más comunes en el parque {parque} son:')  #ejer 2.24
        pprint(n_ejem.most_common(5))   #ejer 2.24
        print('\n\n\n')

        print(f'En el parque {parque} la altura maxima de un ejemplar es de {prop[0]}m y la altura promedio {prop[1]}m')  #ejer 2.25
        print('\n\n\n')

        print(f'La inclinacion maxima en el parque {parque} es de {max_inclinacion[0]} grados, de un ejemplar de la especie {max_inclinacion[1]}')  #ejer 2.27
        print('\n\n\n')

        print(f'La inclinacion promedio maxima en el parque {parque} es de {max_prom_inc[0]} grados de la especie {max_prom_inc[1]}')  #ejer 2.28
        print('\n\n\n')

    except ValueError:  #atrapa listas vacias
        print(f'La especie {especie} no existe en el parque {parque}')