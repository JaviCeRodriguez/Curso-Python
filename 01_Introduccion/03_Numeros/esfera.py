# Escribí un programa llamdo esfera.py en el dirctorio de trabajo que le pida al usuario que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

import math

pi = math.pi

print('Ingrese radio de esfera:', end=' ')
r = float(input())
volumen = (4/3)*pi*(r**3)
print('Volumen de esfera:', round(volumen,4))
