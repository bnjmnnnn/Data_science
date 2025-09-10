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

#Calcular el promedio de cada estudiante y el promedio final del curso
promedio_general = df_estudiantes["promedio"].mean()
print(f"El promedio general del curso es: {promedio_general:.2f}")

# Encontrar estudiante con promedio más alto
estudiante_promedio_mas_alto = df_estudiantes.loc[df_estudiantes["promedio"].idxmax()]
print(f"El promedio más alto es: {estudiante_promedio_mas_alto['promedio']:.2f} (Estudiante: {estudiante_promedio_mas_alto['nombre']})")

# Encontrar estudiante con promedio más bajo
estudiante_promedio_mas_bajo = df_estudiantes.loc[df_estudiantes["promedio"].idxmin()]
print(f"El promedio más bajo es: {estudiante_promedio_mas_bajo['promedio']:.2f} (Estudiante: {estudiante_promedio_mas_bajo['nombre']})")