# ///---- arboles.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

# ! IMPORTANTE: Estaba siguiente una version vieja del repositorio del curso. Es
# ! posible que haya diferencias con lo pedido en las clases 2 y 3

# ///---- Imports ----///
import csv
from collections import Counter
import os
import numpy as np
import matplotlib.pyplot as plt

# ///---- Variables ----///
parques = list()
head = list()
cantidad = Counter()
alturas = list()
maxs = list()
proms = list()
inclinaciones = list()
masincli = list()

# Funcion leer_arbol
def leer_arboles(nombre_archivo):
    file = open(nombre_archivo, 'rt', encoding = "utf8")
    rows = csv.reader(file)
    header = next(rows)

    indices = [header.index(col) for col in header]
    arboleda = [{col: row[index] for col, index in zip(header, indices)} for row in rows]

    return arboleda

#/////////////////////////////////////////////////////////////////////////////

# Funcion leer_parque
def leer_parque(nombre_archivo, parque):
    # Variables internas
    space = list() # Creo la lista para guardar todos los datos
    greenday = list() # Creo la lista con diccionario objetivo
    
    # Abro archivo 'nombre_archivo'
    file = open(nombre_archivo, 'rt', encoding = "utf8")
    rows = csv.reader(file)
    header = next(rows) # Guardo cabezera en header
    
    # Leo el resto de las lineas
    for row in rows:
        green = dict(zip(header, row))
        space.append(green)
        if green["espacio_ve"] == parque:
            greenday.append(green)
    
    # Cierro archivo 'nombre_archivo
    file.close()
    
    # Retorno con informacion requerida
    return (greenday)

#/////////////////////////////////////////////////////////////////////////////

# Funcion especies
def especies(lista_arboles):
    # Variables internas
    pokemon = list() # Lista para adquirir las especies de arboles
    ditto = list () # Lista con posibles especies duplicadas
    
    # Itero sobre la lista
    for TipoPlanta in lista_arboles:
        ditto.append(TipoPlanta["nombre_com"]) # Agrego a una lista todas las especies en el parque
    pokemon = set(ditto) # Elimino duplicados 
    
    # Retorno con informacion requerida
    return (pokemon)

#/////////////////////////////////////////////////////////////////////////////

# Funcion contar_ejemplares
def contar_ejemplares(lista_arboles):
    # Variables internas
    contEspecies = Counter()
    
    # Itero sobre la lista
    for cant in lista_arboles:
        contEspecies[cant['nombre_com']] += 1
        
    # Retorno con informacion requerida
    return (contEspecies)

#/////////////////////////////////////////////////////////////////////////////

# Funcion obtener_alturas
def obtener_alturas(lista_arboles, especie):
    # Variables internas
    jirafales = list() # Lista de alturas de la especie
    
    for planta in lista_arboles:
        if planta['nombre_com'] == especie:
            jirafales.append(float(planta['altura_tot']))
    
    # Retorno con informacion requerida
    return (jirafales)

#/////////////////////////////////////////////////////////////////////////////

# Funcion obtener_inclinaciones
def obtener_inclinaciones(lista_arboles, especie):
    # Variables internas
    inclinaciones = list() # Lista de inclinaciones de la especie
    
    for planta in lista_arboles:
        if planta['nombre_com'] == especie:
            inclinaciones.append(float(planta['inclinacio']))
    
    # Retorno con informacion requerida
    return (inclinaciones)

#/////////////////////////////////////////////////////////////////////////////

# Funcion especimen_mas_inclinado
def especimen_mas_inclinado(lista_arboles):
    # Variables internas
    MasIncli = list() # Lista para guardar especie e inclincacion
    ref = 0 # Referencia para la inclinacion
    
    for planta in lista_arboles:
        if ref <= float(planta['inclinacio']):
            ref = float(planta['inclinacio'])
            especie = planta['nombre_com']
            MasIncli = [especie, ref]

    # Retorno con informacion requerida
    return (MasIncli)

#/////////////////////////////////////////////////////////////////////////////

# Funcion especie_promedio_mas_inclinada
def especie_promedio_mas_inclinada(lista_arboles):
    # Variables internas
    PlanIncli = list() # Lista con todas las inclinaciones
    especimens = list() # Lista de especies
    
    especimens = especies(lista_arboles)
    for especie in especimens:
        incli = obtener_inclinaciones(lista_arboles, especie)
        PlanIncli.append(round(sum(incli)/float(len(incli)),2))
    MasIncliP = dict(zip(especimens, PlanIncli))
    
    # Retorno con informacion requerida
    return (MasIncliP)

#/////////////////////////////////////////////////////////////////////////////

# ///---- Main ----///
# Descomentar para hacerlo manual
# print("Ingrese 3 parques:")
# for x in range(3):
#     park = input(f'Ingrese nombre del parque {x+1}: ') # Ingreso parque
#     head.append(park) # Agrego parque seleccionado en una lista

# arbolObj = input ("Ingrese especie de arbol para analizar: ")

head = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO'] 
arbolObj = 'Jacarandá'

for x in range(3):
    # Leo informacion sobre cada parque
    SouthPark = leer_parque('Data/arbolado-en-espacios-verdes.csv', head[x]) 
    # Obtengo las especies en el parque
    especie = especies(SouthPark)
    # Obtengo la cantidad de especies y las 5 mas frecuentes. Luego
    #guardo las cantidades en una lista
    cantidad = contar_ejemplares(SouthPark)
    frecuentes = cantidad.most_common(5)
    parques.append(cantidad)
    # Obtengo alturas de una especie en los parques, hago promedio y averiguo
    #el arbol mas alto en cada uno
    altura = obtener_alturas(SouthPark, arbolObj)
    maximo = max(altura)
    maxs.append(maximo)
    promedio = round(sum(altura)/float(len(altura)),2)
    proms.append(promedio)
    # Obtengo las inclinaciones de los arboles
    inclinaciones.append(obtener_inclinaciones(SouthPark, arbolObj))
    # Averiguo especie mas inclinada
    masinclin = especimen_mas_inclinado(SouthPark)
    # Averiguo la especie que en promedio es la mas inclinada en c/parque
    masincli = especie_promedio_mas_inclinada(SouthPark)

# ///---- Clase 3 ----///
# Leo el archivo y obtengo información de la arboleda en ciudad
arboleda = leer_arboles('Data/arbolado-en-espacios-verdes.csv')
# Obtengo lista de tuplas con alturas y diametros de una especie
altos=[float(arbol['altura_tot']) for arbol in arboleda] # 3.19

AltDiam = np.array([(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == arbolObj]) # 3.20

# Metodo tradicional para 3.21
DataEspecies={}
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
for especie in especies:
    alturas=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    diametro=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especie]
    DataEspecies[especie] = (alturas, diametro)

#print(DataEspecies[especies[0]][0]) # Para testear

# ///---- Clase 4 ----///
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')

plt.hist(altos,bins=100)
plt.title("Histograma sobre alturas de Jacarandás de ciudad")

plt.figure()
plt.scatter(AltDiam[:,1], AltDiam[:,0], c=np.random.rand(len(AltDiam)), alpha=0.5)
plt.xlabel("Diametro [cm]")
plt.ylabel("Alto [m]")
plt.title("Relación diámetro-alto para Jacarandás")

plt.figure()
for x, especie in enumerate(especies):
    plt.subplot(131+x)
    plt.scatter(tuple(DataEspecies[especies[x]][1]), tuple(DataEspecies[especies[x]][0]), alpha=0.5)
    plt.xlabel("Diametro [cm]")
    plt.ylabel("Alto [m]")
    plt.title(f"Relación diámetro-alto para {especie}")
    plt.xlim(0,max(DataEspecies[especies[0]][1])+10)
    plt.ylim(0,max(DataEspecies[especies[0]][0])+5) 

plt.show() # Muestro los 3 graficos