# Escribí un programa llamdo esfera.py en el dirctorio de trabajo que le pida
#al usuario que ingrese por teclado el radio r de una esfera y calcule e
#imprima el volumen de la misma. Sugerencia: recordar que el volúmen de una
#esfera es 4/3 πr^3.

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

import math #Incluyo libreria math
pi = math.pi # Guardo en una variable el valor pi

print('Ingrese radio de esfera:', end=' ')
r = float(input()) # Pido al usuario que ingrese el radio
volumen = (4/3)*pi*(r**3) # Calculo de volumen
print('Volumen de esfera:', round(volumen,4)) # Imprimo en pantalla

#           Prueba en terminal:
#Ingrese radio de esfera: 3
#Volumen de esfera: 113.0973
