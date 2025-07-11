from data_preprocessing import train_test
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    t_t = train_test()
    X_train = t_t.X_train
    X_test = t_t.X_test
    Y_train = t_t.Y_train
    Y_test = t_t.Y_test
    numeric_features = t_t.numeric_features
    categorical_features = t_t.categorical_features
    preprocessor = t_t.preprocessor

    # Entrenar el modelo Random Forest (el que tuvo mejor rendimiento)
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(preprocessor.fit_transform(X_train), Y_train)

    # Obtener la importancia de las características
    feature_importances = rf_model.feature_importances_


    # Obtener los nombres de las características después del preprocesamiento
    # Esto es un poco más complejo debido al OneHotEncoder

    # Nombres de las características numéricas
    feature_names = numeric_features

    # Nombres de las características categóricas después del OneHotEncoder
    # Obtener las categorías de cada columna categórica
    for i, col in enumerate(categorical_features):
        ohe_categories = preprocessor.named_transformers_['cat'].categories_[i]
        feature_names.extend([f'{col}_{cat}' for cat in ohe_categories])

    # Crear un DataFrame para visualizar la importancia de las características
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    print("Características más Importantes (Random Forest)")
    print(importance_df.head(50).to_string())
    

    top_n = 15
    top_features = importance_df.head(top_n)

    # Crear el gráfico de barras horizontal
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x="Importance",
        y="Feature",
        data=top_features,
        hue="Feature",
        palette="Blues_d",
        dodge=False,
        legend=False
    )
    plt.title("Top 15 Características más Importantes (Random Forest)")
    plt.xlabel("Importancia")
    plt.ylabel("Característica")
    plt.tight_layout()
    plt.show()





