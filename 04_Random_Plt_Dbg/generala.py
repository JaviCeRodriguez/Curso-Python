# ///---- generala.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

# ACLARACION: Este programa está pensando para tomar los menores valores que más repitan en el primer
# tiro y tomarlo como referencia. Ejemplo:
# Tengo en el primer tiro: [2, 1, 3, 2, 3] <== Tomo 2 de valor 2, tiro 3 dados
# Segundo tiro: [3, 3, 3] <== No hay 2, tiro devuelta
# Tercer tiro: [2, 2, 2] <== Todos son 2, generala! :D

# ///---- Imports ----///
import random

# ///---- Tirar ----///
def tirar(n):
    tirada = list()
    for i in range(n): # Realizo 5 tiradas de dados
        tirada.append(random.randint(1,6))
    return (tirada)

# ///---- Es generala ----///
def es_generala():
    n = 5 # Numero de dados
    tiradas_realizadas = 0 # Contador de tiradas
    numero = 0 # Variable para tomar de referencia el que mas repite en 1er tirada

    while ((n != 0) & (tiradas_realizadas < 3)): # Mientras que tenga dados para tirar y no haya superado las 3 tiradas
        guardado = [0]*6    # Genero lista inicial para contar las que repiten
        tirada = tirar(n)   # Hago una nueva tirada de n dados
        for i in range(1, 7): # Recorro los valores del dado (1 al 6)
            for valor in tirada:
                if valor == i:
                    guardado[i-1] += 1   #Si el valor i está en la tirada, incremento esa posición de guardado

        if tiradas_realizadas == 0: # Si estoy en la primera tirada
            cant_max = max(guardado) # Obtengo la máxima cantidad de repeticiones, para quitar esa cantidad de dados en la próxima tirada
            numero = guardado.index(cant_max) + 1 # Obtengo el número que más tiradas tuvo
            n -= cant_max
        else:
            n -= guardado[numero-1] # Para las demás jugadas, quito dados según la cantidad que tenga el index máximo obtenido en la primera tirada
        tiradas_realizadas += 1
        
    if (tiradas_realizadas == 2) and (n == 0):
        return True
    return False

# ///---- Main ----///
N = 10000
G = sum([es_generala() for i in range(N)])
prob = G/N
print(f'Realicé {N} juegos , de los cuales {G} saqué generala en 3 tiros.')
print(f'Podemos estimar que la probabilidad de sacar generala es de {prob*100:.3f}%.')