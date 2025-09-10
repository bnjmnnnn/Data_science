def limpiar_datos(lista_estudiantes):
    """
    Limpia y valida los datos de estudiantes
    """
    # Verificar si la lista está vacía
    if not lista_estudiantes:
        print("⚠️ Advertencia: La lista de estudiantes está vacía.")
        return []
    
    estudiantes_limpios = []
    estudiantes_eliminados = []
    
    for estudiante in lista_estudiantes:
        # Verificar que el estudiante tenga nombre y notas
        if not isinstance(estudiante, dict) or 'nombre' not in estudiante or 'notas' not in estudiante:
            estudiantes_eliminados.append(f"Estudiante sin estructura válida: {estudiante}")
            continue
            
        nombre = estudiante['nombre']
        notas = estudiante['notas']
        
        # Verificar que el nombre no esté vacío
        if not nombre or nombre.strip() == "":
            estudiantes_eliminados.append(f"Estudiante sin nombre válido: {estudiante}")
            continue
            
        # Verificar que tenga notas
        if not notas or len(notas) == 0:
            estudiantes_eliminados.append(f"Estudiante {nombre}: Sin notas")
            continue
            
        # Limpiar notas inválidas (negativas, mayores a 7, None, etc.)
        notas_limpias = []
        notas_removidas = []
        
        for nota in notas:
            try:
                nota_num = float(nota)
                if nota_num < 0:
                    notas_removidas.append(f"{nota} (negativa)")
                elif nota_num > 7:
                    notas_removidas.append(f"{nota} (mayor a 7)")
                else:
                    notas_limpias.append(nota_num)
            except (ValueError, TypeError):
                notas_removidas.append(f"{nota} (no numérica)")
        
        # Si después de limpiar no quedan notas válidas, eliminar estudiante
        if len(notas_limpias) == 0:
            estudiantes_eliminados.append(f"Estudiante {nombre}: Todas las notas son inválidas")
            continue
            
        # Si se removieron notas, informar
        if notas_removidas:
            print(f"⚠️ Estudiante {nombre}: Se removieron notas inválidas: {notas_removidas}")
            
        # Agregar estudiante con datos limpios
        estudiantes_limpios.append({
            'nombre': nombre.strip(),
            'notas': notas_limpias
        })
    
    # Mostrar resumen de limpieza
    if estudiantes_eliminados:
        print("\n❌ Estudiantes eliminados por datos inválidos:")
        for eliminado in estudiantes_eliminados:
            print(f"   - {eliminado}")
    
    
    return estudiantes_limpios

estudiantes = [
    {"nombre": "Ana", "notas": [-6.5, 7.0, 5.8]}, {"nombre": "Pedro", "notas": [4.3, 5.1, 6.7]}, {"nombre": "María", "notas": [3.8, 4.9, 5.5]}, {"nombre": "Javier", "notas": [6.0, 6.4, 5.2]},
    {"nombre": "Camila", "notas": [5.7, 6.1, 4.8]}, {"nombre": "Felipe", "notas": [3.2, 2.0, 4.1]}, {"nombre": "Valentina", "notas": [6.8, 6.2, 6.5]}, {"nombre": "Cristóbal", "notas": [4.4, 5.9, 5.0]},
    {"nombre": "Sofía", "notas": [5.5, 4.7, 6.3]}, {"nombre": "Matías", "notas": [2.0, 3.5, 4.2]}, {"nombre": "Josefa", "notas": [6.9, 7.0, 6.3]}, {"nombre": "Tomás", "notas": [5.0, 4.6, 5.8]}, 
    {"nombre": "Antonia", "notas": [2.0, 4.2, 2.9]}, {"nombre": "Diego", "notas": [6.1, 5.5, 5.9]}, {"nombre": "Constanza", "notas": [4.9, 5.8, 6.4]}, {"nombre": "Ignacio", "notas": [3.4, 4.0, 3.9]},
    {"nombre": "Fernanda", "notas": [6.7, 6.8, 5.9]}, {"nombre": "Sebastián", "notas": [2.0, 3.8, 4.1]}, {"nombre": "Isidora", "notas": [5.6, 6.2, 6.0]}, {"nombre": "Nicolás", "notas": [4.0, 4.8, 3.7]},
    {"nombre": "Paula", "notas": [6.3, 5.5, 6.1]}, {"nombre": "Andrés", "notas": [3.1, 2.4, 4.3]}, {"nombre": "Catalina", "notas": [5.9, 6.4, 5.7]}, {"nombre": "Rodrigo", "notas": [4.6, 3.9, 5.1]},
    {"nombre": "Gabriel", "notas": [2.9, 3.5, 4.4]}, {"nombre": "Daniela", "notas": [5.4, 6.2, 5.8]}, {"nombre": "Vicente", "notas": [3.3, 4.1, 3.6]},
    {"nombre": "Montserrat", "notas": [6.5, 6.9, 6.0]}, {"nombre": "Benjamín", "notas": [4.2, 5.0, 4.7]}
]
