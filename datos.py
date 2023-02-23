import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('mediciones.xlsx')

frecuencia = df['frecuencia']

# Angulos desde -90° a -15°
ang1 = pd.DataFrame.to_numpy(df.iloc[[0],[7,6,5,4,3,2]])

# Angulo 0°
ang0 = pd.DataFrame.to_numpy(df.iloc[[0],[1]])

# Angulos desde 15° a 90°
ang2 = pd.DataFrame.to_numpy(df.iloc[[0],[2,3,4,5,6,7]])

angulos_1 = np.hstack((ang1,ang0,ang2))
# angulo_0 = df['angulo_0']
# angulo_15 = df['angulo_15']
# angulo_30 = df['angulo_30']
# angulo_45 = df['angulo_45']
# angulo_60 = df['angulo_60']
# angulo_75 = df['angulo_75']
# angulo_90 = df['angulo_90']

X_frec , Y_ang = np.meshgrid(frecuencia, angulos_1)

# Matriz de 13x806

magnitudes = np.matrix()