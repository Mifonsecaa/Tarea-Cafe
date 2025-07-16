import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from data_preprocessing import train_test

# Cargar el modelo y el preprocesador
rf_model = joblib.load("rf_model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

# Cargar los datos de prueba originales usando la función del preprocesamiento
t_t = train_test()
X_test = t_t.X_test
Y_test = t_t.Y_test


# Preprocesar los datos de prueba con el preprocesador cargado
X_test_processed = preprocessor.transform(X_test)

# Realizar predicciones
Y_pred = rf_model.predict(X_test_processed)

# Gráfico de dispersión: Valores Reales vs. Predicciones
plt.figure(figsize=(10, 6))
y_test_values = Y_test.values.flatten()
sns.scatterplot(x=y_test_values, y=Y_pred)
plt.plot([y_test_values.min(), y_test_values.max()], [y_test_values.min(), y_test_values.max()], color="red", linestyle="--")
plt.title("Valores Reales vs. Predicciones (Random Forest)")
plt.xlabel("Puntaje de Taza Real")
plt.ylabel("Puntaje de Taza Predicho")
plt.grid(True)
plt.tight_layout()

# Gráfico de Residuales
residuals = y_test_values - Y_pred

plt.figure(figsize=(10, 6))
sns.scatterplot(x=Y_pred, y=residuals)
plt.axhline(y=0, color="red", linestyle="--")
plt.title("Gráfico de Residuales (Random Forest)")
plt.xlabel("Puntaje de Taza Predicho")
plt.ylabel("Residuales")
plt.grid(True)
plt.tight_layout()

plt.show()



plt.show()