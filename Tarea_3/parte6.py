from parte1 import df_pokemones, df_pokemones2
import pandas as pd
import polars as pl

#Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
promedio_x_tipo = df_pokemones.groupby('Tipo 1')['Ataque'].mean()
print(f"Promedio de ataque de los pokemones agrupados por Tipo 1: {promedio_x_tipo}")
mediana_x_tipo = df_pokemones.groupby('Tipo 1')['Ataque'].median()
print(f"Mediana de ataque de los pokemones agrupados por Tipo 1: {mediana_x_tipo}")
desviacion_x_tipo = df_pokemones.groupby('Tipo 1')['Ataque'].std()
print(f"La desviación estándar del ataque de los pokemones agrupados por Tipo 1: {desviacion_x_tipo}")

#¿Qué tipo tiene el mayor promedio de velocidad?
mayor_prom_velocidad = df_pokemones.groupby('Tipo 1')['Velocidad'].mean()
print(f"El tipo con mayor promedio de velocidad es: {mayor_prom_velocidad.idxmax()} con una velocidad de {mayor_prom_velocidad.max()}")

#Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
mayor_PS_x_tipo = df_pokemones.groupby('Tipo 1')['PS'].max()
menor_PS_x_tipo = df_pokemones.groupby('Tipo 1')['PS'].min()
print(f"Mayor PS de cada tipo: {mayor_PS_x_tipo}")
print(f"Menor PS de cada tipo: {menor_PS_x_tipo}")