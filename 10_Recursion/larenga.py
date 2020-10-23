# ///---- larenga.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

def pascal(n, k):
    '''
    A partir de n, k >= 0, hallo el valor solicitado
    en el triangulo de Pascal
    n: fila, k: columna
    '''
    if (k == 0) or (n == k): # Caso base (fila 0 es 1 y tambien los lados)
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

print(pascal(3, 1))

# Si (n, k) = (2, 1) = 2, entonces 2 = 1 + 1 = (1, 0) + (1, 1)
# Si (n, k) = (3, 1) = 3, entonces 3 = 1 + 2 = (2, 0) + (2, 1) = (2, 0) + (1, 0) + (1, 1)