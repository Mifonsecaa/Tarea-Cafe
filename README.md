
# 🟫 Proyecto de Análisis de Café

Este repositorio contiene código y datos para el análisis de calidad del café usando modelos de machine learning como Random Forest Regressor.

El objetivo de este proyecto es predecir la calidad del café, medida por el 'Puntaje de Taza', utilizando datos históricos de la tostadora "Campesino". Se analizaron los datos proporcionados en tres archvios Excel, se realizó un preprocesamiento adecuado se entrenaron modelos de regresión y se analizó la explicabilidad de los resultados para identificar las variables más influyentes.

---

## ⚙️ Configuración del Entorno

Se recomienda seguir los siguientes pasos para configurar correctamente el entorno de desarrollo en tu IDE (por ejemplo, PyCharm, VSCode, etc.):

### 1. Crear e importar el intérprete virtual

1. Abrir el proyecto en su IDE.
2. Ir a la configuración de intérpretes (`Python Interpreter`).
3. Hacer clic en **"Add New Interpreter"** o **"Add Interpreter"**.
4. Seleccione el tipo: `VirtualEnv`.
5. En **Base interpreter**, selecciona: `Python 3.12.3`.
6. Cree el entorno virtual (`venv`) y espere a que se configure.

### 2. Instalar las dependencias

Con el entorno virtual activado, abra una terminal y ejecute:

```bash
pip install -r requirements.txt
