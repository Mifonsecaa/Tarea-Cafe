import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Cargar el modelo y el preprocesador
rf_model = joblib.load("rf_model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

# Cargar los datos de prueba
X_test_processed = pd.read_csv("X_test_processed.csv")
Y_test = pd.read_csv("Y_test.csv")

# Realizar predicciones
Y_pred = rf_model.predict(X_test_processed.values)

# Gráfico de dispersión: Valores Reales vs. Predicciones
plt.figure(figsize=(10, 6))
sns.scatterplot(x=Y_test.values.flatten(), y=Y_pred)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color="red", linestyle="--")
plt.title("Valores Reales vs. Predicciones (Random Forest)")
plt.xlabel("Puntaje de Taza Real")
plt.ylabel("Puntaje de Taza Predicho")
plt.grid(True)
plt.tight_layout()




# Gráfico de Residuales
residuals = Y_test.values.flatten() - Y_pred

plt.figure(figsize=(10, 6))
sns.scatterplot(x=Y_pred, y=residuals)
plt.axhline(y=0, color="red", linestyle="--")
plt.title("Gráfico de Residuales (Random Forest)")
plt.xlabel("Puntaje de Taza Predicho")
plt.ylabel("Residuales")
plt.grid(True)
plt.tight_layout()



plt.show()