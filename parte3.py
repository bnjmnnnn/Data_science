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

# 3. Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes
todas_las_notas = df_estudiantes["notas"].explode()
moda_notas = todas_las_notas.mode()
print(f"La(s) nota(s) más frecuente(s): {list(moda_notas)}")