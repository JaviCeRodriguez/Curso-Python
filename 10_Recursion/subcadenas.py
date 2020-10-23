# Ejercicio 10.5

def posiciones(a, b):
    index_found = []
    if len(a) < len(b): # Caso base
        return index_found

    if a[-len(b):] == b: # Caso recursivo
        index_found.append(a.index(b, -len(b)))
        index_found += posiciones(a[:-1], b) 
        return index_found

    else:
        return posiciones(a[:-1], b)

# print(posiciones('tete', 'te')[::-1])
print(posiciones('Un tete a tete con Tete', 'te')[::-1])