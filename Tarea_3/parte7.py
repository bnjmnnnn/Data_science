from parte1 import df_pokemones, df_pokemones2
import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.

plt.figure(figsize=(10, 6))
sns.swarmplot(data=df_pokemones, x='Tipo 1', y='Ataque', size=6)
plt.title('Ataque por Tipo - Todos los puntos visibles')
plt.xticks(rotation=45)
plt.show()
#Como se puede observar en el gráfico los pokemon tipo lucha tienden a tener más ataque y sus valores parten desde 80 puntos de ataque manteniendo
#sus valores entre 80 y 140, los pokemon tipo dragon poseen valores altos de ataque, los tipo fuego tienen varios puntos en valores altos de ataque
#Y por último los tipo roca en los cuales la mayoría de sus pokemones tiene un alto valor de ataque.
plt.figure(figsize=(10, 6))
sns.swarmplot(data=df_pokemones, x='Tipo 1', y='Defensa', size=6)
plt.title('Defensa por tipo - Todos los puntos visibles')
plt.xticks(rotation=45)
plt.show()
#Como se aprecia en el gráfico los pokemon tipo roca y tierra la mayoría de sus datos están por sobre 100 puntos de defensa 
#lo cual indica que son mas resistentes

#Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
correlacion = df_pokemones['Ataque'].corr(df_pokemones['Velocidad'])
print(f"El coeficiente de correlación entre el ataque y la velocidad de los pokemones es: {correlacion} lo que indica que existe correlación positiva pero débil")

#¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)

desviacion_PS_x_tipo = df_pokemones.groupby('Tipo 1')['PS'].std()
print(f"La desviación estándar agrupadas por tipo es : {desviacion_PS_x_tipo}")

#Identifica posibles outliers en los valores de ataque y PS usando boxplots.
df_pokemones.boxplot(column='Ataque', by='Tipo 1')
plt.show()
#En este gráfico se identifican 2 outliers, uno tipo tierra superior al boxplot y otro tipo normal inferior al boxplot
df_pokemones.boxplot(column='PS', by='Tipo 1')
plt.show()
#En este se pueden apreciar 2 outliers, ambos de tipo normal superior al boxplot

