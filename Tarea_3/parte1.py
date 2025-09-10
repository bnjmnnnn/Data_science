import polars as pl
import numpy as np
import pandas as pd

df_pokemones = pd.read_csv(r"C:\Users\benja\OneDrive\Documentos\GitHub\Data_science\Tarea_3\pokemones_limpios.csv", encoding="latin1")
df_pokemones2 = pl.read_csv(r"C:\Users\benja\OneDrive\Documentos\GitHub\Data_science\Tarea_3\pokemones_limpios.csv", encoding="latin1")