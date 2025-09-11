import polars as pl
import numpy as np
import pandas as pd
from limpieza import limpiar_datos_pokemon
import os

def cargar_datos_pokemon(archivo_original):
    """
    Carga datos Pokémon, aplicando limpieza automáticamente si es necesario
    """
    # Determinar rutas
    ruta_base = os.path.dirname(archivo_original)
    nombre_archivo = os.path.basename(archivo_original)
    nombre_sin_ext = os.path.splitext(nombre_archivo)[0]
    archivo_limpio = os.path.join(ruta_base, f"{nombre_sin_ext}_limpio.csv")
    
    # Verificar si existe archivo limpio y si está actualizado
    necesita_limpieza = True
    if os.path.exists(archivo_limpio):
        # Comparar fechas de modificación
        time_original = os.path.getmtime(archivo_original)
        time_limpio = os.path.getmtime(archivo_limpio)
        
        if time_limpio >= time_original:
            print(f"✅ Usando archivo limpio existente: {archivo_limpio}")
            necesita_limpieza = False
        else:
            print(f"🔄 Archivo original más reciente, aplicando limpieza...")
    else:
        print(f"🧹 No existe archivo limpio, aplicando limpieza...")
    
    # Aplicar limpieza si es necesario
    if necesita_limpieza:
        print("Ejecutando limpieza de datos...")
        limpiar_datos_pokemon(archivo_original)
    
    # Cargar datos limpios
    try:
        df_pandas = pd.read_csv(archivo_limpio, encoding="latin1")
        df_polars = pl.read_csv(archivo_limpio, encoding="latin1")
        
        print(f"📊 Datos cargados: {df_pandas.shape[0]} filas, {df_pandas.shape[1]} columnas")
        print(f"🔍 Columnas disponibles: {list(df_pandas.columns)}")
        
        return df_pandas, df_polars
        
    except Exception as e:
        print(f"❌ Error cargando datos limpios: {e}")
        return None, None

# CONFIGURACIÓN
ARCHIVO_POKEMON = r"C:\Users\benja\OneDrive\Documentos\GitHub\Data_science\Tarea_3\pokemones.csv"

# CARGAR DATOS
print("🚀 Iniciando carga de datos Pokémon...")
df_pokemones, df_pokemones2 = cargar_datos_pokemon(ARCHIVO_POKEMON)

if df_pokemones is not None:
    print("\n📋 MUESTRA DE DATOS (Pandas):")
    print(df_pokemones.head())
    
    print("\n📋 MUESTRA DE DATOS (Polars):")
    print(df_pokemones2.head())
    
    print("\n📈 INFORMACIÓN BÁSICA:")
    print(f"  - Tipos de datos (Pandas): {df_pokemones.dtypes.to_dict()}")
    print(f"  - Memoria usada: {df_pokemones.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    print("\n🎯 ¡Datos listos para análisis!")
else:
    print("❌ No se pudieron cargar los datos")

