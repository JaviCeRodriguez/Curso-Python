# Ejercicio 10.2

def triangular(n):
    suma = 0
    if n == 1: # Caso base
        return 1
    else: # Caso recursivo
        suma += triangular(n-1) + n
        return suma

num = 5

print(triangular(num))