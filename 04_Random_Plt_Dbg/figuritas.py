# ///---- figuritas.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

# ///-------- Datos --------///
# 1) Álbum con 670 figuritas.
# 2) Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
# 3) Cada paquete trae cinco figuritas.

# ///---- Imports ----///
import random
import numpy as np
import matplotlib.pyplot as plt

# ///---- Variables ----///
figus_total = 670 # Cantidad de figuritas en album
figus_paquete = 5 # Cantidad de figuritas en paquete
n_repeticiones = 100 # Veces para analizar llenado de album
paquete = [] # Lista para paquete de figuritas

# ///---- Crear album ----///
def crear_album(figus_total):
    album_make = np.zeros(figus_total, dtype=np.int64)
    return (album_make)

# ///---- Album incompleto ----///
def album_incompleto(A):
    B = A.copy() # Copio la lista para no modificar el original
    B = np.sort(B) # Ordeno de menor a mayor la cantidad de cada figurita
    if B[0] == 0:
        return True # Devuelvo True si faltan
    return False # Devuelvo False si esta completo

# ///---- Comprar figurita----///
def comprar_figu(figus_total):
    figu = random.randint(1,figus_total)
    return figu

# ///---- Comprar paquete ----///
def comprar_paquete(figus_total, figus_paquete):
    pack = np.array([0]*figus_paquete) # Genero vector para 5 figuritas
    for i in range(figus_paquete-1): # Genero 5 figuritas aleatorias 
        pack[i] = random.randint(1,figus_total)
    return pack

# ///---- Compra simulada ----///
def cuantas_figus(figus_total):
    cant_compras = 0
    album = crear_album(figus_total) # Creo album
    while album_incompleto(album) == True:
        compra = comprar_figu(figus_total)
        cant_compras += 1
        album[compra-1] += 1
    return cant_compras

# ///---- Compra simulada (Paquete de 5)----///
def cuantos_paquetes(figus_total, figus_paquete):
    cant_compras = 0
    album = crear_album(figus_total) # Creo album
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        cant_compras += 1
        for i in range(figus_paquete-1):
            album[paquete[i]-1] += 1
    return cant_compras

# ///---- Main ----///
# Experimentos
exp_figus = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio_figus = np.mean(exp_figus)
exp_packs = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio_packs = np.mean(exp_packs)
pack850 = np.sum([1 for i in range(n_repeticiones) if cuantos_paquetes(figus_total, figus_paquete) <= 850])

# Prints
print (f'\nCompra de figus en promedio: {promedio_figus} figuritas')
print (f'Compra de paquetes en promedio: {promedio_packs} paquetes')
print (f'De {n_repeticiones} experimentos, en solo {pack850:.0f} se necesitaron hasta 850 paquetes para llenar el album')
print (f'La probabilidad de poder comprar hasta 850 paquetes es de {(pack850/n_repeticiones)*100}%')

# Plots
plt.hist(exp_packs,bins=150)
plt.ylabel('Probabilidad')
plt.xlabel('Paquetes')
plt.show()