# soluciones_de_errores.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

#%%
# Ejercicio 3.1: Semántica
#def tiene_a(expresion):
#    n = len(expresion)
#    i = 0
#    while i<n:
#        if expresion[i] == 'a':
#            print(f'Detecto {expresion[i]}')
#            return True
#        else:
#            print('No')
#            return False
#        i += 1

#tiene_a('UNSAM 2020')
#tiene_a('abracadabra')
#tiene_a('La novela 1984 de George Orwell')

# Para este ejercicio, probé dos cosas a partir de los problemas vistos:
#   1) Comenté los return debido a que solo me detectaba el primer caracter de la cadena (cosa que esta mal)
#   2) Coloqué un print para cada caso del if, para chequear si se cumple el condicional

# Codigo corregido ():
def tiene_a(expresion):
   n = len(expresion)
   i = 0
   while i<n:
       if expresion[i] == 'a':
           print(f'Detecto {expresion[i]}') # Para testear
           return True
       else:
           print('No') # Para testear
           #return False # Lo comento para que no salga del while al leer el primer char
       i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#---------------------------------------------------------------------------------------------
#%%
# Ejercicio 3.2: Sintaxis
#def tiene_a(expresion)
#    n = len(expresion)
#    i = 0
#    while i<n
#        if expresion[i] == 'a'
#            return True
#        i += 1
#    return Falso

#tiene_a('UNSAM 2020')
#tiene_a('La novela 1984 de George Orwell')

# En este ejercicio, se detectaron errores de sintaxis en:
#   1) Linea 'def tiene_a(expresion) (faltaba :)
#   2) Linea while i<n (faltaba :)
#   3) Linea if expresion[i] == 'a' (faltaba :)
#   4) return Falso (Falso no es lo mismo que False)

# Codigo corregido:
def tiene_a(expresion):
   n = len(expresion)
   i = 0
   while i<n:
       if expresion[i] == 'a':
           #print('Si detecta') # Para testear
           return True
       i += 1
   return False
#---------------------------------------------------------------------------------------------
#%%
# Ejercicio 3.3: Tipos
# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#             print(tiene)
#         i += 1
#     return tiene

# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984)

# En este ejercicio, a simple vista se ve que tiene_uno(1984) está mal. Meto
#en la función un dato tipo int en lugar de un tipo string. Esto se soluciona
#colocando comillas.

# Codigo corregido:
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
            print(tiene)
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')
#---------------------------------------------------------------------------------------------
#%%
# Ejercicio 3.4: Alcances
# def suma(a,b):
#     c = a + b
    
# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")

# Acá, si corremos el programa, nos indica que 2 + 3 = None

# Codigo corregido:
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#---------------------------------------------------------------------------------------------
#%%
# Ejercicio 3.5: Pisando memoria
# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)

# El problema aca es que se pisan los valores de una fila con la anterior. Esto se debe a que
#se le da un valor a cada registro[encabezado[n]], que en este caso son los valores de la 
#ultima fila del archivo.

# Codigo corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado, (fila[0], int(fila[1]), float(fila[2]))))
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)