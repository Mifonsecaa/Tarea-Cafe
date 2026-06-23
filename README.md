# Proyecto de Análisis de Calidad del Café

## Descripción del Proyecto

Este repositorio contiene el código y los datos para un proyecto de análisis de la calidad del café, utilizando modelos de Machine Learning. El objetivo principal es predecir el "Puntaje de Taza" del café basándose en datos históricos de la tostadora "Campesino". El proyecto abarca desde el preprocesamiento de datos hasta el entrenamiento y evaluación de modelos de regresión, con un enfoque en la identificación de las variables más influyentes en la calidad del café.

## Características Principales

*   **Análisis Predictivo**: Implementación de modelos de regresión, incluyendo Regresión Lineal y Random Forest Regressor, para predecir el puntaje de taza del café.
*   **Procesamiento de Datos**: Incluye scripts para la preparación, preprocesamiento y análisis exploratorio de datos provenientes de archivos Excel.
*   **Evaluación de Modelos**: Métricas como R2 Score, Mean Absolute Error (MAE) y Mean Squared Error (MSE) son utilizadas para evaluar el rendimiento de los modelos.
*   **Análisis de Importancia de Características**: Identificación de las variables clave que influyen en la calidad del café.
*   **Tecnologías**: Desarrollado en Python, utilizando bibliotecas como `pandas`, `scikit-learn`, y `joblib` para la persistencia de modelos.

## Estructura del Repositorio

El repositorio se organiza de la siguiente manera:

*   `data/`: Contiene los archivos de datos de entrada (Excel).
*   `src/`: Contiene los scripts principales del proyecto:
    *   `analisis_exp.py`: Script para el análisis exploratorio de datos.
    *   `data_preparation.py`: Script para la preparación inicial de los datos.
    *   `data_preprocessing.py`: Script para el preprocesamiento de los datos, incluyendo la división en conjuntos de entrenamiento y prueba.
    *   `feature_importance.py`: Script para analizar la importancia de las características.
    *   `model_training.py`: Script para el entrenamiento de los modelos de regresión.
    *   `performance.py`: Script para la evaluación del rendimiento de los modelos.
    *   `preprocessor.joblib`: Objeto preprocesador serializado.
    *   `rf_model.joblib`: Modelo Random Forest entrenado y serializado.
*   `Scripts/`: Contiene scripts de activación de entorno virtual (Windows y Linux).
*   `Reporte.pdf`: Documento con el reporte final del proyecto.
*   `requirements.txt`: Lista de dependencias del proyecto.

## Instalación y Configuración

Para configurar el entorno del proyecto y ejecutar los scripts, siga los siguientes pasos:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Mifonsecaa/Tarea-Cafe.git
cd Tarea-Cafe
```

### 2. Crear y Activar un Entorno Virtual

Se recomienda el uso de un entorno virtual para gestionar las dependencias del proyecto.

**En Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**En macOS y Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

Con el entorno virtual activado, instale todas las bibliotecas necesarias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Preparar los Datos

Los archivos de datos originales deben colocarse en la carpeta `data/`. El proyecto espera tres archivos Excel de la tostadora "Campesino".

## Uso

Los scripts en la carpeta `src/` pueden ejecutarse en secuencia para replicar el análisis:

1.  **Preparación y Preprocesamiento de Datos**: Ejecute `data_preparation.py` y `data_preprocessing.py` para limpiar y transformar los datos.
2.  **Análisis Exploratorio**: Ejecute `analisis_exp.py` para obtener insights iniciales de los datos.
3.  **Entrenamiento de Modelos**: Ejecute `model_training.py` para entrenar los modelos de regresión.
4.  **Evaluación de Rendimiento**: Ejecute `performance.py` para evaluar los modelos entrenados.
5.  **Importancia de Características**: Ejecute `feature_importance.py` para identificar las variables más relevantes.

## Resultados y Conclusiones

El `Reporte.pdf` contiene un resumen detallado de los hallazgos, incluyendo la comparación de rendimiento entre los modelos de Regresión Lineal y Random Forest, así como las conclusiones sobre las características más influyentes en la calidad del café. El proyecto demuestra la aplicación de técnicas de Machine Learning para la toma de decisiones basada en datos en la industria del café.

## Autor

Miguel Fonseca

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo `LICENSE` para más detalles.

