import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('mediciones.xlsx')

# Vector de frecuencias
frecuencia = df['frecuencia']

# Angulos desde -90° a -15°
ang1 = pd.DataFrame.to_numpy(df.iloc[[0],[7,6,5,4,3,2]])

# Angulo 0°
ang0 = pd.DataFrame.to_numpy(df.iloc[[0],[1]])

# Angulos desde 15° a 90°
ang2 = pd.DataFrame.to_numpy(df.iloc[[0],[2,3,4,5,6,7]])

# Vector de angulos
angulos_1 = np.hstack((ang1,ang0,ang2))

# Crear matriz de 13x806
X_frec , Y_ang = np.meshgrid(frecuencia, angulos_1)

# Matriz de 13x806
magnitudes = np.zeros(np.shape(X_frec))

# Recorrido de cada fila de Magnitudes (i), de 0 a 13
# y de las columnas (j) tiene que ser de -90° a 90°
# es decir, de la columna -90°, hasta la 0° y vuelta hasta +90°.
# Esto es, que recorra las columnas del dataframe 
# 7,6,5,4,3,2,1,-6,-5,-4,-3,-2,-1. Este vector será el que
# haga recorrer j

vector1_j = np.arange((int(len(magnitudes)/2)+1),0,-1) # Desde 7 hasta 1

vector2_j = np.arange(-(int(len(magnitudes)/2)),0,1) # Desde -6 hasta -1

vector_j = np.hstack((vector1_j,vector2_j))

# Bucle que recorre de 0 a 12 (filas de Magnitudes), a la vez que toma
# los valores del array Vector_j, que será el que vaya seleccionando
# las columnas del DataFrame según la necesidad

for i, j in zip(range(magnitudes.shape[0]), vector_j):
    magnitudes[i, :] = df.iloc[:, j]

# Arrays para conformar los ejes

ang_axis = np.transpose([-90,-75,-60,-45,-30,-15,0,15,30,45,60,75,90])

frec_axis = np.transpose(frecuencia)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Angles [ °]")
graf = plt.contourf(frec_axis,ang_axis,magnitudes)
cbar = plt.colorbar(graf)


