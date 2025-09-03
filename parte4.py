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

# 4. Porcentaje de estudiantes con al menos una nota bajo 4.0
estudiantes_con_bajo4 = df_estudiantes[df_estudiantes["notas"].apply(lambda x: any(nota < 3.95 for nota in x))]
porcentaje_bajo4 = (len(estudiantes_con_bajo4) / len(df_estudiantes)) * 100
print(f"Porcentaje de estudiantes con al menos 1 nota < 4.0: {porcentaje_bajo4:.2f}%")