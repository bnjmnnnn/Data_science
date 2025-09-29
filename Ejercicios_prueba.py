import pandas as pd
import numpy as np
from statistics import multimode
from collections import Counter
Datos = {'Nombre': ["Ana", "Luis", "Sofía", "Pedro"],
         'Edad':[28, 35, 22, 41],
         'Ciudad': ["Santiago", "Valparaiso", "Concepción", "Santiago"],
         'Compras': [5, 2, 7, 1]}

df = pd.DataFrame(Datos)

#Escribe el código para filtrar y mostrar solo los clientes de Santiago que hayan realizado más de 3 compras.
clientes_filtrados = df[(df['Ciudad'] == 'Santiago') & (df['Compras'] > 3)]
print(clientes_filtrados)
# Escribe el código para calcular la edad promedio de los clientes de cada ciudad.
edad_promedio = df.groupby('Ciudad')['Edad'].mean()
print(edad_promedio)
#Escribe el código para añadir una columna llamada Segmento que diga "Frecuente" si las compras son 5 o más, y "Ocasional" en caso contrario.
df['Segmento'] = df['Compras'].apply(lambda x: 'Frecuente' if x >= 5 else 'Ocasional')
print(df)

estudiantes = [ {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]}, {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]}, {"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]}, {"nombre": "Pedro", "notas": [5.5, 6.1, 5.9]} ]
#a) Escribe el código para calcular el promedio general de notas del curso.
todas_notas = [nota for est in estudiantes for nota in est["notas"]]
promedio = sum(todas_notas) / len(todas_notas)
print(promedio)

notas2 = np.array([4.5, 6.2, 3.9, 7.0, 5.5, 2.1])
promedi = notas2.std()
print(promedi)

mayores = notas2[notas2>=4]
print(mayores)

inventario = {
    "Codigo_Producto": ["LAP-01", "MOU-03", "TEC-02", "MON-05"],
    "Stock_Inicial": [50, 120, 80, 40],
    "Unidades_Vendidas": [15, 80, 45, 10],
    "Costo_Unitario": [600000, 10000, 30000, 120000]
}

df_inventario = pd.DataFrame(inventario)
#a) Escribe el código para añadir una nueva columna llamada Stock_Final, calculada como Stock_Inicial - Unidades_Vendidas. Muestra cómo quedaría la tabla final.
df_inventario['Stock_Final'] = df_inventario['Stock_Inicial'] - df_inventario['Unidades_Vendidas']
print(df_inventario)
#b) Escribe el código para filtrar y mostrar solo los productos con un Stock_Final menor a 30 unidades.
filtrado = df_inventario[(df_inventario['Stock_Final'] < 30)]
print(filtrado)
#c) Escribe el código para calcular el valor total del inventario vendido, que sería la suma de (Unidades_Vendidas * Costo_Unitario).
valor_total = df_inventario['Unidades_Vendidas'] * df_inventario['Costo_Unitario']
print(valor_total)

# ...existing code...

ventas = {
    "Producto": ["Laptop", "Mouse", "Laptop", "Teclado"],
    "Vendedor": ["Ana", "Luis", "Sofía", "Pedro"],
    "Unidades": [3, 10, 2, 5],
    "Precio_Unitario": [700000, 12000, 680000, 25000]
}

df_ventas = pd.DataFrame(ventas)
print(df_ventas)

Total_unidades = df_ventas.groupby('Producto')['Unidades']
print(Total_unidades)

ventas_enero = np.array([100, 150, 200, 250]) 
ventas_febrero = np.array([120, 130, 210, 240])
#a) Escribe el código para calcular el crecimiento absoluto de ventas de cada producto (febrero - enero).
crecimiento = ventas_febrero - ventas_enero
#b) Escribe el código para calcular el porcentaje de crecimiento de cada producto.
porcentaje = ((ventas_febrero - ventas_enero) / ventas_enero) * 100

estudiantes_universidad = {
    "Nombre": ["Ana", "Juan", "Sofía"],
    "Edad": [22, 25, 23],
    "Carrera": ["Ing. Civil", "Ing. Informática", "Ing. Civil"]
}

df_estudiantes = pd.DataFrame(estudiantes_universidad)

#a) Escribe el código para seleccionar solo la columna "Carrera".

df_carrera = df_estudiantes['Carrera']
print(df_carrera)
#b) Escribe el código para filtrar y mostrar solo los alumnos mayores de 22 años.)
mayores = df_estudiantes[(df_estudiantes['Edad'] > 22)]
print(mayores)

notas3 = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0, 6.5]
#a) Escribe el código para contar cuántos estudiantes están en cada tramo: reprobados (<4.0), aprobados (4.0-5.9), y destacados (≥6.0).
aprobados = 0 
reprobados = 0 
destacados = 0 
for nota in notas3:
    if nota < 4.0:
        reprobados +=1
    elif nota > 4.0 and nota < 6.0:
        aprobados +=1
    elif nota >= 6.0:
        destacados +=1
print(f"Cantidad de aprobados: {aprobados}, cantidad de destacados: {destacados}, cantidad de reprobados {reprobados}")
#b) Escribe el código para calcular el promedio de cada grupo.