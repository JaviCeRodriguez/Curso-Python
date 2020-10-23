# ///---- envido.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import random

# ///---- Variables ----///
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
suma = 0
N = 100000000
envidos = [0]*3 # Variable para guardar envidos de 31, 32 y 33

# ///---- Cuento envido ----///
# Gracias a Ezequiel Canay por esta parte del code
def contar_envido(mano):
    # Variables
    palos = ['oro', 'copa', 'espada', 'basto']
    envido = 0

    #! Sin flor
    for palo in palos: # Analizo cada palo
        cant = 0 # Variable para contar cartas de un palo
        palito = 0 # Variable para detectar si hay palo en mano
        list_mano = [0]*3 # Uso una lista para hacer operaciones con cada palo
        for i, carta in enumerate(mano): # Analizo la mano. carta = (valor, palo)
            if (carta[1] == palo) and (carta[0] < 10): # Chequeo si la carta es el palo a analizar y si es menor a 10
                list_mano[i] = carta[0]
                cant += 1
                palito = 1
        if (envido == 0) and (palito == 1): # Si envido es 0, tomo de referencia el palo detectado
            envido = sum(list_mano)
            if envido != 0: # Si envido sigue siendo 0, es porque hay negras
                envido += 20
        elif (palito == 1) and ((sum(list_mano)+20) > envido): # De un palo, consegui 1 o 2 carta/s (1 al 7)
            envido = sum(list_mano)+20

    #! Con flor
    # for palo in palos:
    #     aux = 0
    #     n = 0
    #     for carta in mano: # carta = (valor, palo)
    #         if carta[1] == palo:
    #             if carta[0] < 10:
    #                 aux += carta[0]
    #                 n += 1
    #     if n>=1:
    #         aux += 20
    #     if aux > envido:
    #         envido = aux

    return envido

# ///---- Main ----///
for i in range(N):
    if (N%10000 == 0):
        print(N)
    mazo = [(valor,palo) for valor in valores for palo in palos] # Genero mazo de 40 cartas
    #random.shuffle(mazo) # Mezclo el mazo
    mano = random.sample(mazo,k=3) # Obtengo mazo sin reposicion
    #print (f'Tengo la siguiente mano: {mano}')
    #print(contar_envido(mano))
    if (contar_envido(mano) == 31):
        envidos[0] += 1
    if (contar_envido(mano) == 32):
        envidos[1] += 1
    if (contar_envido(mano) == 33):
        envidos[2] += 1

print(f'Hice {N} jugadas, de las cuales obtuve: ')
print(f'\t# Envido de 31, con {(envidos[0]/N)*100:.3f}%')
print(f'\t# Envido de 32, con {(envidos[1]/N)*100:.3f}%')
print(f'\t# Envido de 33, con {(envidos[2]/N)*100:.3f}%')