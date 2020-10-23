# ///---- termometro.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import random
import numpy as np

# ///---- Variables ----///
n = 999 # Cantidad de mediciones
media = 0 # Media
desvio = 0.2 # Desvio estandar
temp = 37.5 # Temperatura real
medi = list() # Lista vacia para guardar l|a mediana

# ///---- Distribucion ----///
def distribucion(n, mu , sigma, medreal):
    # Variable local
    distrib = list()

    # Obtengo errores de medicion
    # Aclaracion: Como usan 1 decimal, tomaria 1 decimal de error
    #pero estaria perdiendo informacion. Tomo 3 decimales
    for i in range(n):
        distrib.append(round(random.normalvariate(mu,sigma)+medreal, 3))
    return distrib # Retorno con valores de la distribucion

# ///---- Main ----///
print ('\nMediciones de temperatura: ', end=' ')
valores = np.array(distribucion(n, media, desvio, temp))
print (valores)
np.save('Data\Temperaturas.npy', valores)
maximo = max(valores)
print ('\nValor maximo de las mediciones: ', maximo)
minimo = min(valores)
print ('\nValor minimo de las mediciones: ', minimo)
promedio = round(sum(valores)/n, 3)
print ('\nValor promedio de las mediciones: ', promedio)
medi = np.sort(valores)
mediana = medi[n//2]
print ('\nLa mediana de las mediciones: ', mediana)
