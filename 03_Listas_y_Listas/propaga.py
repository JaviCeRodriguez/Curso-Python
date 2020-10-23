# propaga.py

# Alumno: Javier Ceferino Rodriguez
# E-mail: javicerodriguez@gmail.com

# ///---- Invierto lista ----///
def invertir_lista(lista):
    listaInv = []
    N = len(lista)
    
    for i in range(N-1,-1,-1):
        l = lista[i]
        listaInv.append(l)
    return listaInv

# ///---- Propagacion de fosforo prendido ----///
def propagar (fosforos):
    fosforosN1 = []
    fosforosN2 = []
    N = len(fosforos) # Tomo longitud de fosforos
    flag = 0 # Uso flag para detectar fosforos encendidos

    # Recorro lista hacia la derecha
    for i in range(0, N):
        f = fosforos[i]
        if f == 1:
            flag = 1
        if f == -1:
            flag = 0
        if (f == 0) and (flag == 1):
            fosforosN1.append(1)
        else:
            fosforosN1.append(f)

    print(fosforosN1)

    # Recorro lista hacia la izquierda
    for i in range(N-1, -1, -1):
        f = fosforosN1[i]
        if f == 1:
            flag = 1
        if f == -1:
            flag = 0
        if (f == 0) and (flag == 1):
            fosforosN2.append(1)
        else:
            fosforosN2.append(f)
    fosforosN2 = invertir_lista(fosforosN2)

    return fosforosN2

fosforosAntes = [0, 0, -1, 0, 1, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, 0]
print(fosforosAntes)
fosforosDespues = propagar(fosforosAntes)
print(fosforosDespues)