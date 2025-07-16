from data_preparation import data_merged
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from collections import namedtuple
import numpy as np
import datetime

df_merged = data_merged()

# Eliminar filas con valores nulos en 'Puntaje_Taza'
df_merged.dropna(subset=['Puntaje_Taza'], inplace=True)


# Identificar variables de entrada (X) y variable objetivo (Y)
Y = df_merged['Puntaje_Taza']

T_t = namedtuple("t_t", ["X_train", "X_test", "Y_train", "Y_test", "numeric_features", "categorical_features", "preprocessor", "X_final"])

def train_test(verbose=None):
    if verbose is None:
        verbose = __name__ == "__main__"

    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)
    # Seleccionar características que parecen relevantes y no filtran información
    X = df_merged[[
        'Humedad',
        'Mallas',
        'Verificacion_Fisica',
        'Origen',
        'Variedad',
        'Proceso',
        'Beneficio',
        'Peso_Verde',
        'Merma',
        'Peso_Tostado',
        'Perfil',
        'Temp_Inicio_Final',
        'Tiempo_Tueste'
    ]].copy() # Usar .copy() para evitar SettingWithCopyWarning

    vprint(f"NaNs before numeric conversion:\n{X.isnull().sum()}\n")

    # Convertir tipos de datos si es necesario
    X['Humedad'] = pd.to_numeric(X['Humedad'], errors='coerce')
    X['Mallas'] = pd.to_numeric(X['Mallas'], errors='coerce')
    X['Peso_Verde'] = pd.to_numeric(X['Peso_Verde'], errors='coerce')
    X['Merma'] = pd.to_numeric(X['Merma'], errors='coerce')
    X['Peso_Tostado'] = pd.to_numeric(X['Peso_Tostado'], errors='coerce')

    vprint(f"NaNs after numeric conversion:\n{X.isnull().sum()}\n")

    # Imputar valores nulos con la media para columnas numéricas
    for col in ['Humedad', 'Mallas', 'Peso_Verde', 'Merma', 'Peso_Tostado']:
        if X[col].isnull().any():
            X[col] = X[col].fillna(X[col].mean())

    vprint(f"NaNs after initial numeric imputation:\n{X.isnull().sum()}\n")


    # Para 'Temp_Inicio_Final', extraer temperaturas numéricas
    def extract_temps(temp_str):
        if isinstance(temp_str, str):
            # Limpiar la cadena de caracteres no numéricos y dividir
            temp_str_cleaned = temp_str.replace('°', '').replace(',', '.')  # Reemplazar coma por punto para decimales
            temps = []
            for s in temp_str_cleaned.split('/'):
                try:
                    temps.append(float(s.strip()))
                except ValueError:
                    temps.append(np.nan)  # Asignar NaN si no se puede convertir

            if len(temps) == 2:
                return pd.Series(temps)
        return pd.Series([np.nan, np.nan])


    X[['Temp_Inicio', 'Temp_Final']] = X['Temp_Inicio_Final'].apply(extract_temps)
    X.drop('Temp_Inicio_Final', axis=1, inplace=True)

    vprint(f"NaNs after Temp_Inicio_Final extraction:\n{X.isnull().sum()}\n")

    # Imputar valores nulos para las nuevas columnas de temperatura
    for col in ['Temp_Inicio', 'Temp_Final']:
        if X[col].isnull().any():
            X[col] = X[col].fillna(X[col].mean())

    vprint(f"NaNs after Temp_Inicio_Final imputation:\n{X.isnull().sum()}\n")

    # Para 'Tiempo_Tueste', convertir a minutos (o segundos si es necesario)
    def time_to_minutes(time_val):
        if isinstance(time_val, datetime.time):
            return time_val.hour * 60 + time_val.minute + time_val.second / 60
        elif isinstance(time_val, str):
            parts = time_val.split(':')
            if len(parts) == 2:
                try:
                    minutes = int(parts[0])
                    seconds = int(parts[1])
                    return minutes + seconds / 60
                except ValueError:
                    pass
        return np.nan

    vprint(f"Unique values in Tiempo_Tueste before conversion: {X['Tiempo_Tueste'].unique()}\n")
    X['Tiempo_Tueste_Minutos'] = X['Tiempo_Tueste'].apply(time_to_minutes)
    X.drop('Tiempo_Tueste', axis=1, inplace=True)

    vprint(f"NaNs after Tiempo_Tueste conversion:\n{X.isnull().sum()}\n")

    # Imputar valores nulos para 'Tiempo_Tueste_Minutos'
    if X['Tiempo_Tueste_Minutos'].isnull().any():
        X['Tiempo_Tueste_Minutos'] = X['Tiempo_Tueste_Minutos'].fillna(X['Tiempo_Tueste_Minutos'].mean())

    vprint(f"NaNs after Tiempo_Tueste imputation:\n{X.isnull().sum()}\n")

    # Identificar columnas numéricas y categóricas
    # Excluir 'Notas_Catacion' ya que es texto libre y no es fácil de procesar para regresión simple
    # Excluir 'Verificacion_Fisica' ya que es 'C' para todos los valores no nulos, no aporta variabilidad

    # Actualizar X para incluir las nuevas columnas numéricas y excluir las que no se usarán
    X_final = X[[
        'Humedad',
        'Mallas',
        'Origen',
        'Variedad',
        'Proceso',
        'Beneficio',
        'Peso_Verde',
        'Merma',
        'Peso_Tostado',
        'Perfil',
        'Temp_Inicio',
        'Temp_Final',
        'Tiempo_Tueste_Minutos'
    ]]

    vprint(f"NaNs in X_final before preprocessing:\n{X_final.isnull().sum()}\n")

    # Columnas numéricas y categóricas para el preprocesamiento
    numeric_features = [
        'Humedad',
        'Mallas',
        'Peso_Verde',
        'Merma',
        'Peso_Tostado',
        'Temp_Inicio',
        'Temp_Final',
        'Tiempo_Tueste_Minutos'
    ]
    categorical_features = [
        'Origen',
        'Variedad',
        'Proceso',
        'Beneficio',
        'Perfil'
    ]

    # Crear el preprocesador
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, Y_train, Y_test = train_test_split(X_final, Y, test_size=0.2, random_state=42)
    return T_t(X_train, X_test, Y_train, Y_test, numeric_features, categorical_features, preprocessor, X_final)

if __name__ == "__main__":
    t_t = train_test()
    X_train = t_t.X_train
    X_test = t_t.X_test
    Y_train = t_t.Y_train
    Y_test = t_t.Y_test
    numeric_features = t_t.numeric_features
    categorical_features = t_t.categorical_features
    preprocessor = t_t.preprocessor

    # Aplicar el preprocesador a los datos de entrenamiento y prueba
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    # Convertir a array denso para poder usar np.isnan y guardar en CSV
    X_train_processed_dense = X_train_processed.toarray()
    X_test_processed_dense = X_test_processed.toarray()

    print(f"NaNs in X_train_processed: {np.isnan(X_train_processed_dense).sum()}\n")
    print(f"NaNs in X_test_processed: {np.isnan(X_test_processed_dense).sum()}\n")

    # Guardar los conjuntos preprocesados para el siguiente paso
    pd.DataFrame(X_train_processed).to_csv('X_train_processed.csv', index=False)
    pd.DataFrame(X_test_processed).to_csv('X_test_processed.csv', index=False)
    pd.DataFrame(Y_train).to_csv('Y_train.csv', index=False)
    pd.DataFrame(Y_test).to_csv('Y_test.csv', index=False)

    print("Preprocesamiento de datos completado. Datos guardados en X_train_processed.csv, X_test_processed.csv, Y_train.csv, Y_test.csv")