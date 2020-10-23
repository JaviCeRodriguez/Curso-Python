import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

directorio = 'Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
# print(df.head(10))

# print(df.columns)

# print(df.describe())

# print(df['nombre_com'].unique())

# print((df['nombre_com'] == 'Ombú').sum())

# cant_ejemplares = df['nombre_com'].value_counts()
# print(cant_ejemplares.head(10))

# cols = ['altura_tot', 'diametro', 'inclinacio']
# df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
# print(df_jacarandas)
# # df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')
# sns.scatterplot(data= df_jacarandas, x = 'diametro', y = 'altura_tot')
# plt.show()

# print(df.iloc[0:4])

# print(pd.date_range('20200923 14:00', periods = 6, freq = 'H'))

# print(pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H')))

# idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
# s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
# s2 = s1.cumsum()
# # s2.plot()
# # plt.figure()
# w = 5 # ancho en minutos de la ventana
# s3 = s2.rolling(w).mean()
# # s3.plot()
# df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
# df_series_23.plot()
# plt.show()

# horas = 8
# idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
# nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
# df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
# # df_walks.plot()
# w = 45
# df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
# nsuav = ['S_' + n for n in nombres]
# df_walk_suav.columns = nsuav # cambio el nombre de las columnas
#                              # para los datos suavizados
# df_walk_suav.plot()
# plt.show()
# df_walk_suav.to_csv('.\Data\caminata_apostolica.csv')