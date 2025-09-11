import polars as pl
import pandas as pd
from parte1 import df_pokemones, df_pokemones2
import matplotlib.pyplot as plt

#Haz un histograma de los valores de ataque.
#Realiza un gráfico de dispersión entre ataque y velocidad.
#Haz un boxplot de los PS por tipo principal (Tipo 1).
#Grafica la distribución de la defensa usando un diagrama de violín.

df_pokemones['Ataque'].hist()
plt.show()

df_pokemones.plot.scatter(x='Ataque', y='Velocidad')
plt.title("Gráfico de Dispersión con Pandas y Matplotlib")
plt.xlabel("Ataque")
plt.ylabel("Velocidad")
plt.show()

df_pokemones.boxplot(column='PS', by='Tipo 1')
plt.show()

plt.violinplot(df_pokemones['Defensa'])
plt.title("Gráfico de Violín de la distribución de la defensa")
plt.ylabel("Valores")
plt.show()