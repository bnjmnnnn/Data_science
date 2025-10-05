import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

datos = {'Superficie_m2': [50, 70, 65, 90, 45], 'Num_Habitaciones': [1, 2, 2, 3, 1], 'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0], 'Precio_UF': [2500, 3800, 3500, 5200, 2100]}

df = pd.DataFrame(datos)

X = df[['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km']]
Y = df['Precio_UF']

# 3. Dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# 4. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, Y_train)

# 5. Hacer predicciones
Y_pred = modelo.predict(X_test)

rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
r2 = r2_score(Y_test, Y_pred)

print(f'\n RESULTADOS DE LA EVALUACIÓN - PREDICCIÓN DE EL PRECIO UF\n')
print(f'RMSE: {rmse:.2f}')
print(f'   → En promedio, las predicciones se desvían en {rmse:.2f} goles del resultado real')

print(f'\n📈 R²: {r2:.2f} ({r2:.0%})')
print(f'   → El modelo explica el {r2:.0%} de la variabilidad en los goles marcados')