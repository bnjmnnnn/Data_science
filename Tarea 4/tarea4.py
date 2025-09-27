import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1 Datos y DataFrame
#Fueron recopilados de https://www.campeonatochileno.cl y https://www.sofascore.com/es/equipo/futbol/universidad-de-chile/3161#tab:statistics
datos = {'Goles_Marcados_X_Fecha': [5, 1, 1, 2, 1, 0, 2, 3, 3, 1, 5, 0, 6, 0, 3, 2, 4, 0, 4, 1, 0,],
         'Goles_partido_anterior': [0, 5, 1, 1, 2, 1, 0, 2, 3, 3, 1, 5, 0, 6, 0, 3, 2, 4, 0, 4, 1],
         'Ocasiones_claras_x_fecha': [7, 3, 0, 2, 1, 2, 2, 5, 2, 2, 5, 3, 6, 2, 6, 2, 3, 1, 5, 4, 2],
         'Tiros_puerta_x_fecha': [36, 13, 22, 12, 18, 23, 10, 20, 17, 15, 16, 22, 16, 11, 23, 10, 17, 25, 24, 19, 12]}

df = pd.DataFrame(datos)

# 2. Definir X e Y
X = df[['Goles_partido_anterior', 'Ocasiones_claras_x_fecha', 'Tiros_puerta_x_fecha']]
Y = df['Goles_Marcados_X_Fecha']

# 3. Dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
#print(X_train, X_test, Y_train, Y_test)

# 4. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, Y_train)

# 5. Hacer predicciones
Y_pred = modelo.predict(X_test)

rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
r2 = r2_score(Y_test, Y_pred)

print(f'\n📊 RESULTADOS DE LA EVALUACIÓN - PREDICCIÓN DE GOLES U. DE CHILE:\n')
print(f'🎯 RMSE: {rmse:.2f}')
print(f'   → En promedio, las predicciones se desvían en {rmse:.2f} goles del resultado real')

print(f'\n📈 R²: {r2:.2f} ({r2:.0%})')
print(f'   → El modelo explica el {r2:.0%} de la variabilidad en los goles marcados')

