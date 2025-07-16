
# 🟫 Proyecto de Análisis de Café

Este repositorio contiene código y datos para el análisis de calidad del café usando modelos de machine learning como Random Forest Regressor.

El objetivo de este proyecto es predecir la calidad del café, medida por el 'Puntaje de Taza', utilizando datos históricos de la tostadora "Campesino". Se analizaron los datos proporcionados en tres archivos Excel, se realizó un preprocesamiento adecuado, se entrenararon modelos de regresión y se analizó la explicabilidad de los resultados para identificar las variables más influyentes.
---

## ⚙️ Configuración del Entorno

Se recomienda seguir los siguientes pasos para configurar correctamente el entorno de desarrollo en tu IDE (por ejemplo, PyCharm, VSCode, etc.):

### 1. Crear e importar el intérprete virtual

1. Abre tu proyecto en tu IDE.
2. Ve a la configuración de intérpretes (`Python Interpreter`).
3. Haz clic en **"Add New Interpreter"** o **"Add Interpreter"**.
4. Selecciona el tipo: `VirtualEnv`.
5. En **Base interpreter**, selecciona: `Python 3.12.3`.
6. Crea el entorno virtual (`venv`) y espera a que se configure.

### 2. Instalar las dependencias

Con el entorno virtual activado, abre una terminal y ejecuta:

```bash
pip install -r requirements.txt
