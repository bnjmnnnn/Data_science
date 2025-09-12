from parte1 import df_pokemones, df_pokemones2
import pandas as pd
import polars as pl

#Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa,velocidad y PS.
#Ordena el DataFrame por "Poder Total" de mayor a menor.

#Pandas
df_pokemones['Poder total'] = df_pokemones['Ataque'] + df_pokemones['Defensa'] + df_pokemones['Velocidad'] + df_pokemones['PS']
#print(f"El data frame con el poder total de cada pokemon es: {df_pokemones}") 

df_pokemones = df_pokemones.sort_values("Poder total", ascending=False)
print(df_pokemones)

#Polars
df_pokemones2 = df_pokemones2.with_columns(
    (pl.col("Ataque") + pl.col("Defensa") + pl.col('Velocidad') + pl.col('PS')).alias('Poder Total')
)
#print(f"El data frame con poder total de cada pokemon es: {df_pokemones2}")

df_pokemones2 = df_pokemones2.sort("Poder Total", descending = True)
print(f"El poder total es: {df_pokemones2}")