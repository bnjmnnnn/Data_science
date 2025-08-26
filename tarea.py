estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]}, {"nombre": "Pedro", "notas": [4.3, 5.1, 6.7]}, {"nombre": "María", "notas": [3.8, 4.9, 5.5]}, {"nombre": "Javier", "notas": [6.0, 6.4, 5.2]},
    {"nombre": "Camila", "notas": [5.7, 6.1, 4.8]}, {"nombre": "Felipe", "notas": [3.2, 2.9, 4.1]}, {"nombre": "Valentina", "notas": [6.8, 6.2, 6.5]}, {"nombre": "Cristóbal", "notas": [4.4, 5.9, 5.0]},
    {"nombre": "Sofía", "notas": [5.5, 4.7, 6.3]}, {"nombre": "Matías", "notas": [2.8, 3.5, 4.2]}, {"nombre": "Josefa", "notas": [6.9, 7.0, 6.3]}, {"nombre": "Tomás", "notas": [5.0, 4.6, 5.8]}, 
    {"nombre": "Antonia", "notas": [3.7, 4.2, 2.9]}, {"nombre": "Diego", "notas": [6.1, 5.5, 5.9]}, {"nombre": "Constanza", "notas": [4.9, 5.8, 6.4]}, {"nombre": "Ignacio", "notas": [3.4, 4.0, 3.9]},
    {"nombre": "Fernanda", "notas": [6.7, 6.8, 5.9]}, {"nombre": "Sebastián", "notas": [2.5, 3.8, 4.1]}, {"nombre": "Isidora", "notas": [5.6, 6.2, 6.0]}, {"nombre": "Nicolás", "notas": [4.0, 4.8, 3.7]},
    {"nombre": "Paula", "notas": [6.3, 5.5, 6.1]}, {"nombre": "Andrés", "notas": [3.1, 2.7, 4.3]}, {"nombre": "Catalina", "notas": [5.9, 6.4, 5.7]}, {"nombre": "Rodrigo", "notas": [4.6, 3.9, 5.1]},
    {"nombre": "Francisca", "notas": [6.8, 7.0, 6.6]}, {"nombre": "Gabriel", "notas": [2.9, 3.5, 4.4]}, {"nombre": "Daniela", "notas": [5.4, 6.2, 5.8]}, {"nombre": "Vicente", "notas": [3.3, 4.1, 3.6]},
    {"nombre": "Montserrat", "notas": [6.5, 6.9, 6.0]}, {"nombre": "Benjamín", "notas": [4.2, 5.0, 4.7]}
]
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

aprobados = [estudiante for estudiante in estudiantes if estudiante["promedio"] >= 4.0]
print(f"Estudiantes aprobados: {len(aprobados)}")
for estudiante in aprobados:
    print(f"{estudiante['nombre']}: {estudiante['promedio']}")