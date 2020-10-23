# invlista.py

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

# ///---- Codigo principal ----///
#listaV = [1,2,3,4,5]
listaV = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
listaN = invertir_lista(listaV)
print (listaN)
