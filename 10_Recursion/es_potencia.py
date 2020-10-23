# Ejercicio 10.4

def es_potencia(n, b): # b^x = n ?
    if n == b: # Caso base x = 1
        return True
    if n == 1: # Caso base x = 0
        return True
    if n > b: # Caso recursivo con n mayor a b (potencia: b^x = n?)
        resto = n % b
        if resto == 0:
            return es_potencia(n // b, b)
        else:
            return False
    if n < b: # Caso recursivo con n menor a b (raiz: n^x = b?)
        resto = b % n
        if resto == 0:
            return es_potencia(n, b // n)
        else:
            return False

print(es_potencia(27, 3))