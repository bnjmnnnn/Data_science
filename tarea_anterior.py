from statistics import multimode
from collections import Counter
from datos import estudiantes

# 1. Calcular el promedio de notas de cada estudiante y determinar quién tiene el promedio más alto y más bajo.
# Aquí también resolvemos el item 5, entregando una lista ordenada de mayor a menor de los estudiantes según su promedio.

for estudiante in estudiantes:
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
    estudiante["promedio"] = round(promedio, 2)

estudiantes.sort(key=lambda x: x["promedio"], reverse=True)
promedio_mas_alto = estudiantes[0]
promedio_mas_bajo = estudiantes[-1]
for estudiante in estudiantes:
    print(f"{estudiante['nombre']}: {estudiante['promedio']}")
print("El promedio más alto de todos los estudiantes es:", promedio_mas_alto["promedio"], "y es de", promedio_mas_alto["nombre"])
print("El promedio más bajo de todos los estudiantes es:", promedio_mas_bajo["promedio"], "y es de", promedio_mas_bajo["nombre"])

# 2. Estudiantes con todas las asignaturas aprobadas
aprobados = [estudiante for estudiante in estudiantes if all(nota >= 4.0 for nota in estudiante["notas"])]
print(f"Estudiantes con todas las asignaturas aprobadas >= 4.0: {len(aprobados)}")
for estudiante in aprobados:
    print(f"{estudiante['nombre']}: {estudiante['notas']}")

# 3. Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes

todas_las_notas = [nota for estudiante in estudiantes for nota in estudiante["notas"]]

conteo_notas = Counter(todas_las_notas)

modas = multimode(todas_las_notas)

# Si solo hay una nota como moda, la mostrará. en caso de haber empate, mostrará aquellas como la más frecuente
if len(modas) == 1:
    nota_moda = modas[0]
    print(f"La nota más frecuente es {nota_moda} con {conteo_notas[nota_moda]} apariciones")
else:
    print("Las notas más frecuentes son:")
    for nota_moda in modas:
        print(f"La nota {nota_moda} apareciendo {conteo_notas[nota_moda]} veces")

# 4. Porcentaje de estudiantes con al menos una nota bajo 4.0
total_estudiantes = len(estudiantes)
estudiantes_con_rojos = [estudiante for estudiante in estudiantes if any(nota < 4.0 for nota in estudiante ["notas"])]

cantidad_rojos = len(estudiantes_con_rojos)
porcentaje_rojos = (cantidad_rojos / total_estudiantes) * 100

print(f"Hay {cantidad_rojos} estudiantes con al menos una nota bajo 4.0")
print(f"Equivalente a un {porcentaje_rojos:.2f}% del total")