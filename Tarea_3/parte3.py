import pandas as pd
import polars as pl
from parte1 import df_pokemones, df_pokemones2

#Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
#¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
#¿Cuántos Pokémon tienen dos tipos?
#Calcula el rango y la desviación estándar de los PS (Puntos de Salud).

#Pandas
promedio_ataque = df_pokemones['Ataque'].mean()
mediana_ataque = df_pokemones['Ataque'].median()
moda_ataque = df_pokemones['Ataque'].mode()
print(f"Promedio de ataque: {promedio_ataque}")
print(f"Mediana de ataque: {mediana_ataque}")
print(f"Moda de ataque: {moda_ataque}")

pokemon_mayor_defensa = df_pokemones.loc[df_pokemones['Defensa'].idxmax()]
pokemon_menor_velocidad = df_pokemones.loc[df_pokemones['Velocidad'].idxmin()]
print(f"Pokémon con mayor defensa: {pokemon_mayor_defensa['Nombre']} con una defensa de {pokemon_mayor_defensa['Defensa']}")
print(f"Pokémon con menor velocidad: {pokemon_menor_velocidad['Nombre']} con una velocidad de {pokemon_menor_velocidad['Velocidad']}")

pokemones_bitipo = df_pokemones[df_pokemones['Tipo 2'].notna() & (df_pokemones['Tipo 2'].str.strip() != '')]
print(pokemones_bitipo[['Nombre', 'Tipo 1', 'Tipo 2']])

#pokemon_mayor_PS = df_pokemones.loc[df_pokemones['PS'].idxmax()]
pokemon_mayor_PS = df_pokemones['PS'].max()
#pokemon_menor_PS = df_pokemones.loc[df_pokemones['PS'].idxmin()]
pokemon_menor_PS = df_pokemones['PS'].min()
rango = pokemon_mayor_PS - pokemon_menor_PS
print(f"El rango de los PS es: {rango}")

desviacion_estandar_PS = df_pokemones['PS'].std()
print(f"La desviación estándar es: {desviacion_estandar_PS}")

#Polars
promedio_pokemones = df_pokemones2.group_by('Tipo 1').agg(
    pl.col('Ataque').mean().alias('Ataque promedio')
)
print(promedio_pokemones)
moda_pokemones = df_pokemones2.group_by('Tipo 1'). agg(
    pl.col('Ataque').mode().alias('Moda')
)
print(moda_pokemones)
mediana_pokemones = df_pokemones2.group_by('Tipo 1'). agg(
    pl.col('Ataque').median().alias('Mediana')
)
print(mediana_pokemones)
mayor_defensa = df_pokemones2['Nombre', 'Defensa']
print(f"El pokemon con mayor defensa es: {mayor_defensa.max()}")

menor_velocidad = df_pokemones2['Nombre', 'Velocidad']
print(f"El pokemon con menor velocidad es: {menor_velocidad.min()}")

pokemones_bitipo = (
    df_pokemones2
    .filter(pl.col('Tipo 1').is_not_null() & pl.col('Tipo 2').is_not_null())
)
cantidad = len(pokemones_bitipo)
print(f"Pokemones con 2 tipos: {pokemones_bitipo} y su cantidad es : {cantidad}")
salud_max = df_pokemones['PS'].max()
salud_min = df_pokemones['PS'].min()
rango_PS = salud_max - salud_min
print(f"El rango es: {rango_PS}") 
desviacion_PS = df_pokemones['PS'].std()
print(f"La desviación estándar en base PS es: {desviacion_PS}")

