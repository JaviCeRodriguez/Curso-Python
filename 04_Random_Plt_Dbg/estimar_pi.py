# ///---- termometro.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com
# raiz(r) = raiz(x**2 + y**2)

# ///---- Imports ----///
import math
import random

# ///---- Variables ----///
N = 10000000
M = 0

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

for i in range(0,N):
    (a, b) = generar_punto()
    c = math.sqrt(a**2 + b**2)
    if (c < 1): # Si esta dentro del circulo unitario
        M += 1 #sumo incremento M

print (float((4*M)/N))