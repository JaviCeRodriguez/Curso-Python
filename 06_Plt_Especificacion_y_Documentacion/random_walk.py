import numpy as np
import matplotlib.pyplot as plt

N = 100000              # Largo maximo
cant_trayectos = 12     # Cantidad de trayectos
caminatas = []           # Lista de trayectos
color_list = ['red', 'orangered', 'gray', 'black', 'darkorange', 'yellowgreen', 'lightgreen', 'dodgerblue', 'lime', 'blue', 'darkviolet', 'indigo']

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()


def desvio(walks):
    '''
    Obtengo indices de la lista walks que me indican
    cuales son los que mas y menos desvian
    '''
    index_max = 0   # Numero de caminata en donde hay mayor desvio (0 al 11)
    maximo = 0      # Auxiliar para obtener maximo desvio
    index_min = 0   # Numero de caminata en donde hay menor desvio (0 al 11)
    minimo = 0      # Auxiliar para obtener minimo desvio
    aux = 0         # Variable auxiliar

    trayectos = np.absolute(walks)
    
    for i, trayecto in enumerate(trayectos):
        if i == 0: # Tomo de referencia el maximo de la primera caminata
            maximo = trayecto.max()
            minimo = maximo
        else:
            aux = trayecto.max()
            if aux > maximo:
                index_max = i
            if aux < minimo:
                index_min = i

    return (index_min, index_max)

plt.subplot(2, 2, (1, 2))
for i in range(cant_trayectos):
    caminata = randomwalk(N)
    caminatas.append(caminata)
    plt.plot(caminata, c=color_list[i])
plt.title('Las 12 caminatas al azar')
plt.ylabel('Distancia al origen')
plt.xlabel('Tiempo')

(min_desv, max_desv) = desvio(caminatas)    # Obtengo las caminatas con menor y mayor desvio
print(min_desv, max_desv)                   # Check-in de lo anterior

plt.subplot(2, 2, 3)
plt.plot(caminatas[min_desv], c=color_list[min_desv])
plt.title('Caminata con menor desvio')

plt.subplot(2, 2, 4)
plt.plot(caminatas[max_desv], c=color_list[max_desv])
plt.title('Caminata con mayor desvio')

plt.show()