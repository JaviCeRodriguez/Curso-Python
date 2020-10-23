# ///---- termometro.py ----///
# Alumno: Javier C. Rodriguez
# Mail: javicerodriguez@gmail.com

# ///---- Imports ----///
import numpy as np
import matplotlib.pyplot as plt

# ///---- Main ----///
# Obtencion de datos
mediciones = np.load('Data\Temperaturas.npy')

# Plots
plt.hist(mediciones,bins=100)
plt.ylabel('Probabilidad')
plt.xlabel('Datos')
plt.show()