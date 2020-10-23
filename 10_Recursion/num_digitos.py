# Ejercicio 10.3

def digitos(n):
    dig = 1
    if n < 10: # Caso base
        return 1
    else: # Caso recursivo
        n /= 10
        dig += digitos(n)
        return dig

num = 3234120689132

print (digitos(num))