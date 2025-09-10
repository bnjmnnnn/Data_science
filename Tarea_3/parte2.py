import polars as pl
import pandas as pd
from parte1 import df_pokemones, df_pokemones2
#Filtra todos los Pokémon de tipo "Fuego".
#Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
#Pandas
pokemones_fuego = df_pokemones[(df_pokemones['Tipo 1'] == 'Fuego') | (df_pokemones['Tipo 2'] == 'Fuego')][['Nombre', 'Tipo 1', 'Ataque', 'Velocidad']]
print(pokemones_fuego)

#Polars
pokemones_tipo_fuego = (
    df_pokemones2
    .filter(pl.col('Tipo 1') == 'Fuego')
    .select(['Nombre', 'Tipo 1', 'Ataque', 'Velocidad'])
)
print(pokemones_tipo_fuego)
print(len(pokemones_tipo_fuego))
