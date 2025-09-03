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
promedio_mas_alto = df_estudiantes["promedio"].max()
print(f"El promedio más alto es: {promedio_mas_alto:.2f}" )
promedio_mas_bajo = df_estudiantes["promedio"].min()
print(f"El promedio más bajo es: {promedio_mas_bajo:.2f}")

# 2. Estudiantes con todas las asignaturas aprobadas
df_estudiantes_aprobados = df_estudiantes[df_estudiantes["notas"].apply(lambda x: all(nota >= 3.95 for nota in x))]
print(f"Estudiantes aprobados (todas las notas >= 3.95): {df_estudiantes_aprobados.shape[0]}")

# 3. Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes
todas_las_notas = df_estudiantes["notas"].explode()
moda_notas = todas_las_notas.mode()
print(f"La(s) nota(s) más frecuente(s): {list(moda_notas)}")

# 4. Porcentaje de estudiantes con al menos una nota bajo 4.0
estudiantes_con_bajo4 = df_estudiantes[df_estudiantes["notas"].apply(lambda x: any(nota < 3.95 for nota in x))]
porcentaje_bajo4 = (len(estudiantes_con_bajo4) / len(df_estudiantes)) * 100
print(f"Porcentaje de estudiantes con al menos 1 nota < 4.0: {porcentaje_bajo4:.2f}%")

# 5. Ordenar los promedios de mayor a menor
df_ordenado = df_estudiantes.sort_values("promedio", ascending=False).copy()
df_ordenado["promedio"] = df_ordenado["promedio"].round(2)
print("Estudiantes ordenados por promedio (mayor a menor):")
print(df_ordenado[["nombre", "promedio"]])

#Gráficas los datos te muestra que tan dispersos están algunos datos lo que te puede indicar cuáles son los datos sucios, usar seaborn cuando utilizamos pandas
#Utilizar EDA para verificar que los datos están limpios
