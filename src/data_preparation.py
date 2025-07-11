from analisis_exp import cargar_data
import pandas as pd


dfs = cargar_data()

def data_merged():
    # Cargar los DataFrames limpios
    df_calidad = dfs["CalidadTrillado"]
    df_tostion = dfs["Tostion"]
    df_despachos = dfs["Despachos"]


    # Eliminar las primeras filas que contienen metadatos en df_calidad, df_tostion y df_despachos

    df_calidad = df_calidad.iloc[3:].copy()
    df_tostion = df_tostion.iloc[1:].copy()
    df_despachos = df_despachos.iloc[1:].copy()

    # Renombrar columnas para mayor claridad
    df_calidad.rename(columns={
        df_calidad.columns[0]: 'Fecha_Calidad',
        df_calidad.columns[1]: 'Lote_Calidad',
        df_calidad.columns[2]: 'Denominacion_Marca',
        df_calidad.columns[3]: 'Cantidad_Calidad',
        df_calidad.columns[4]: 'Humedad',
        df_calidad.columns[5]: 'Cumple_Humedad',
        df_calidad.columns[6]: 'Mallas',
        df_calidad.columns[7]: 'Cumple_Mallas',
        df_calidad.columns[8]: 'Verificacion_Fisica',
        df_calidad.columns[9]: 'Notas_Catacion',
        df_calidad.columns[10]: 'Puntaje_Taza',
        df_calidad.columns[11]: 'Puntaje_Final',
        df_calidad.columns[12]: 'Liberacion_Lote',
        df_calidad.columns[13]: 'Responsable_Calidad'
    }, inplace=True)

    df_tostion.rename(columns={
        df_tostion.columns[0]: 'Fecha_Tostion',
        df_tostion.columns[1]: 'Lote_Tostion',
        df_tostion.columns[2]: 'Origen',
        df_tostion.columns[3]: 'Variedad',
        df_tostion.columns[4]: 'Proceso',
        df_tostion.columns[5]: 'Beneficio',
        df_tostion.columns[6]: 'Peso_Verde',
        df_tostion.columns[7]: 'Merma',
        df_tostion.columns[8]: 'Peso_Tostado',
        df_tostion.columns[9]: 'Perfil',
        df_tostion.columns[10]: 'Temp_Inicio_Final',
        df_tostion.columns[11]: 'Tiempo_Tueste',
        df_tostion.columns[12]: 'Observaciones_Tostion',
        df_tostion.columns[13]: 'Tostador'
    }, inplace=True)

    df_despachos.rename(columns={
        df_despachos.columns[0]: 'Pedido',
        df_despachos.columns[1]: 'Fecha_Tueste_Despacho',
        df_despachos.columns[2]: 'Fecha_Empaque',
        df_despachos.columns[3]: 'Tipo_Cafe',
        df_despachos.columns[4]: 'Presentacion',
        df_despachos.columns[5]: 'NaN_Col1',
        df_despachos.columns[6]: 'Cantidad_Despacho',
        df_despachos.columns[7]: 'NaN_Col2',
        df_despachos.columns[8]: 'NaN_Col3',
        df_despachos.columns[9]: 'Cliente',
        df_despachos.columns[10]: 'Responsable_Despacho',
        df_despachos.columns[11]: 'Verifica'
    }, inplace=True)

    # Convertir 'Puntaje_Taza' a numérico en df_calidad
    df_calidad['Puntaje_Taza'] = pd.to_numeric(df_calidad['Puntaje_Taza'], errors='coerce')

    # Unir df_calidad y df_tostion por Lote
    df_merged = pd.merge(df_calidad, df_tostion, left_on='Lote_Calidad', right_on='Lote_Tostion', how='inner', suffixes=('_calidad', '_tostion'))

    return df_merged

if __name__ == "__main__":
    print(data_merged())

