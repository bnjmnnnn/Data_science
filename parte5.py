from datos import estudiantes, limpiar_datos
import pandas as pd
import numpy as np

estudiantes_limpios = limpiar_datos(estudiantes)

# Verificar si quedan estudiantes después de la limpieza
if not estudiantes_limpios:
    print("❌ Error: No hay estudiantes válidos para procesar.")
    exit()
    
# Crear DataFrame con datos limpios
df_estudiantes = pd.DataFrame(estudiantes_limpios)
df_estudiantes["promedio"] = df_estudiantes["notas"].apply(np.mean)


# 5. Ordenar los promedios de mayor a menor
df_ordenado = df_estudiantes.sort_values("promedio", ascending=False).copy()
df_ordenado["promedio"] = df_ordenado["promedio"].round(2)
print("Estudiantes ordenados por promedio (mayor a menor):")
print(df_ordenado[["nombre", "promedio"]])