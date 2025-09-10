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

# 2. Estudiantes con todas las asignaturas aprobadas
df_estudiantes_aprobados = df_estudiantes[df_estudiantes["notas"].apply(lambda x: all(nota >= 3.95 for nota in x))]
print(f"Estudiantes aprobados (todas las notas >= 3.95): {df_estudiantes_aprobados.shape[0]}")