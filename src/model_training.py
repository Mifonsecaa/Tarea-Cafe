import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from data_preprocessing import train_test
import joblib # Para guardar y cargar modelo

# Cargar los datos preprocesados
tt = train_test()
preprocessor = tt.preprocessor
X_train_raw = tt.X_train
X_test_raw = tt.X_test

# Aplicar el preprocesador para obtener los datos procesados en el formato correcto
X_train_processed = preprocessor.fit_transform(X_train_raw)
X_test_processed = preprocessor.transform(X_test_raw)

# Cargar las variables objetivo desde CSV
Y_train = pd.read_csv("Y_train.csv").values.ravel()
Y_test = pd.read_csv("Y_test.csv").values.ravel()

# Inicializar y entrenar el primer modelo: Regresión Lineal
linear_model = LinearRegression()
linear_model.fit(X_train_processed, Y_train)

# Predecir y evaluar el modelo de Regresión Lineal
Y_pred_linear = linear_model.predict(X_test_processed)
r2_linear = r2_score(Y_test, Y_pred_linear)
mae_linear = mean_absolute_error(Y_test, Y_pred_linear)
mse_linear = mean_squared_error(Y_test, Y_pred_linear)

# Inicializar y entrenar el segundo modelo: Random Forest Regressor
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train_processed, Y_train)

# Predecir y evaluar el modelo Random Forest
Y_pred_rf = rf_model.predict(X_test_processed)
r2_rf = r2_score(Y_test, Y_pred_rf)
mae_rf = mean_absolute_error(Y_test, Y_pred_rf)
mse_rf = mean_squared_error(Y_test, Y_pred_rf)

print(f"--- Resultados del Modelo de Regresión Lineal ---\n")
print(f"R2 Score: {r2_linear:.4f}\n")
print(f"Mean Absolute Error (MAE): {mae_linear:.4f}\n")
print(f"Mean Squared Error (MSE): {mse_linear:.4f}\n")

print(f"--- Resultados del Modelo Random Forest Regressor ---\n")
print(f"R2 Score: {r2_rf:.4f}\n")
print(f"Mean Absolute Error (MAE): {mae_rf:.4f}\n")
print(f"Mean Squared Error (MSE): {mse_rf:.4f}\n")

# Guardar el modelo Random Forest y el preprocesador
joblib.dump(rf_model, 'rf_model.joblib')
joblib.dump(preprocessor, 'preprocessor.joblib')

