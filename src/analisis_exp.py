import pandas as pd
from pathlib import Path


def cargar_data():
    BASE_DIR = Path(__file__).resolve().parent



    file_paths = [

        BASE_DIR.parent / "data" / "CC FT 17   Formato de Control de Calidad Café de Trillado (1).xlsx",
        BASE_DIR.parent / "data" / "CC FT 18  Formato de  Tostión (1).xlsx",
        BASE_DIR.parent / "data" / "CC FT 21   Formato de Control de Despachos (1).xlsx"

    ]

    # Nombres para los DataFrames
    df_names = ['CalidadTrillado', 'Tostion', 'Despachos']

    # Diccionario para almacenar los DataFrames
    dataframes = {}

    for i, path in enumerate(file_paths):
        try:
            # Leer hoja1
            df1 = pd.read_excel(path, sheet_name=0, header=4)
            dataframes[df_names[i] + "_hoja1"] = df1

            # Leer hoja2
            df2 = pd.read_excel(path, sheet_name=1, header=4)
            dataframes[df_names[i] + "_hoja2"] = df2
        except Exception as e:
            print(f"Error al leer {path}: {e}")

    return dataframes

if __name__ == "__main__":
    print(cargar_data())


