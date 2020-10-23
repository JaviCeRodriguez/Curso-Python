# ///---- alquiler.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

#///---- Imports ----///
import numpy as np
import matplotlib.pyplot as plt


#///---- ajuste_lineal_simple ----///
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


#///---- Variables ----///
minx = 0
maxx = 200
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

#///---- Ajuste lineal ----///
a, b = ajuste_lineal_simple(superficie, alquiler)

#///---- Tendencia lineal ----///
grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

#///---- Plot ----///
g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'red')
plt.xlabel('x')
plt.ylabel('y')

#///---- Error Cuadratico Medio ----///
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())

#///---- Plot view ----///
plt.show()