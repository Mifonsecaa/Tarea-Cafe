from analisis_exp import cargar_data
import pandas as pd


dfs = cargar_data()

def data_merged():
    # Cargar los DataFrames limpios
    df_calidad_hoja1 = dfs['CalidadTrillado_hoja1']
    df_calidad_hoja2 = dfs['CalidadTrillado_hoja2']
    df_tostion_hoja1 = dfs['Tostion_hoja1']
    df_tostion_hoja2 = dfs['Tostion_hoja2']
    df_despachos_hoja1 = dfs['Despachos_hoja1']
    df_despachos_hoja2 = dfs['Despachos_hoja2']

    # Eliminar las primeras filas que contienen metadatos en df_calidad, df_tostion y df_despachos en la hoja 1

    df_calidad_hoja1 = df_calidad_hoja1.iloc[3:].copy()
    df_tostion_hoja1 = df_tostion_hoja1.iloc[1:].copy()
    df_despachos_hoja1 = df_despachos_hoja1.iloc[1:].copy()

    # Eliminar las primeras filas que contienen metadatos en df_calidad, df_tostion y df_despachos en la hoja 2

    # df_despachos_second: header is 4 (index 3), so actual data starts from index 4 (row 5). So, iloc[4:]
    df_calidad_hoja2 = df_calidad_hoja2.iloc[4:].copy()
    df_tostion_hoja2 = df_tostion_hoja2.iloc[4:].copy()
    df_despachos_hoj2 = df_despachos_hoja2.iloc[4:].copy()

    # Concatenar los DataFrames de las hojas principales y secundarias
    df_calidad_hoja1 = pd.concat([df_calidad_hoja1, df_calidad_hoja2], ignore_index=True)
    df_tostion_hoja1 = pd.concat([df_tostion_hoja1, df_tostion_hoja2], ignore_index=True)
    df_despachos_hoja1 = pd.concat([df_despachos_hoja1, df_despachos_hoja2], ignore_index=True)

    # Renombrar columnas para mayor claridad
    df_calidad_hoja1.rename(columns={
        df_calidad_hoja1.columns[0]: 'Fecha_Calidad',
        df_calidad_hoja1.columns[1]: 'Lote_Calidad',
        df_calidad_hoja1.columns[2]: 'Denominacion_Marca',
        df_calidad_hoja1.columns[3]: 'Cantidad_Calidad',
        df_calidad_hoja1.columns[4]: 'Humedad',
        df_calidad_hoja1.columns[5]: 'Cumple_Humedad',
        df_calidad_hoja1.columns[6]: 'Mallas',
        df_calidad_hoja1.columns[7]: 'Cumple_Mallas',
        df_calidad_hoja1.columns[8]: 'Verificacion_Fisica',
        df_calidad_hoja1.columns[9]: 'Notas_Catacion',
        df_calidad_hoja1.columns[10]: 'Puntaje_Taza',
        df_calidad_hoja1.columns[11]: 'Puntaje_Final',
        df_calidad_hoja1.columns[12]: 'Liberacion_Lote',
        df_calidad_hoja1.columns[13]: 'Responsable_Calidad'
    }, inplace=True)

    df_tostion_hoja1.rename(columns={
        df_tostion_hoja1.columns[0]: 'Fecha_Tostion',
        df_tostion_hoja1.columns[1]: 'Lote_Tostion',
        df_tostion_hoja1.columns[2]: 'Origen',
        df_tostion_hoja1.columns[3]: 'Variedad',
        df_tostion_hoja1.columns[4]: 'Proceso',
        df_tostion_hoja1.columns[5]: 'Beneficio',
        df_tostion_hoja1.columns[6]: 'Peso_Verde',
        df_tostion_hoja1.columns[7]: 'Merma',
        df_tostion_hoja1.columns[8]: 'Peso_Tostado',
        df_tostion_hoja1.columns[9]: 'Perfil',
        df_tostion_hoja1.columns[10]: 'Temp_Inicio_Final',
        df_tostion_hoja1.columns[11]: 'Tiempo_Tueste',
        df_tostion_hoja1.columns[12]: 'Observaciones_Tostion',
        df_tostion_hoja1.columns[13]: 'Tostador'
    }, inplace=True)

    df_despachos_hoja1.rename(columns={
        df_despachos_hoja1.columns[0]: 'Pedido',
        df_despachos_hoja1.columns[1]: 'Fecha_Tueste_Despacho',
        df_despachos_hoja1.columns[2]: 'Fecha_Empaque',
        df_despachos_hoja1.columns[3]: 'Tipo_Cafe',
        df_despachos_hoja1.columns[4]: 'Presentacion',
        df_despachos_hoja1.columns[5]: 'NaN_Col1',
        df_despachos_hoja1.columns[6]: 'Cantidad_Despacho',
        df_despachos_hoja1.columns[7]: 'NaN_Col2',
        df_despachos_hoja1.columns[8]: 'NaN_Col3',
        df_despachos_hoja1.columns[9]: 'Cliente',
        df_despachos_hoja1.columns[10]: 'Responsable_Despacho',
        df_despachos_hoja1.columns[11]: 'Verifica'
    }, inplace=True)

    # Renombrar columnas para las segundas hojas
    df_calidad_hoja2.rename(columns={
        df_calidad_hoja2.columns[0]: 'Fecha_Calidad',
        df_calidad_hoja2.columns[1]: 'Lote_Calidad',
        df_calidad_hoja2.columns[2]: 'Denominacion_Marca',
        df_calidad_hoja2.columns[3]: 'Cantidad_Calidad',
        df_calidad_hoja2.columns[4]: 'Humedad',
        df_calidad_hoja2.columns[5]: 'Cumple_Humedad',
        df_calidad_hoja2.columns[6]: 'Mallas',
        df_calidad_hoja2.columns[7]: 'Cumple_Mallas',
        df_calidad_hoja2.columns[8]: 'Verificacion_Fisica',
        df_calidad_hoja2.columns[9]: 'Notas_Catacion',
        df_calidad_hoja2.columns[10]: 'Puntaje_Taza',
        df_calidad_hoja2.columns[11]: 'Puntaje_Final',
        df_calidad_hoja2.columns[12]: 'Liberacion_Lote',
        df_calidad_hoja2.columns[13]: 'Responsable_Calidad'
    }, inplace=True)

    # df_tostion_second
    df_tostion_hoja2.rename(columns={
        df_tostion_hoja2.columns[0]: 'Fecha_Tostion',
        df_tostion_hoja2.columns[1]: 'Lote_Tostion',
        df_tostion_hoja2.columns[2]: 'Origen',
        df_tostion_hoja2.columns[3]: 'Variedad',
        df_tostion_hoja2.columns[4]: 'Proceso',
        df_tostion_hoja2.columns[5]: 'Beneficio',
        df_tostion_hoja2.columns[6]: 'Peso_Verde',
        df_tostion_hoja2.columns[7]: 'Merma',
        df_tostion_hoja2.columns[8]: 'Peso_Tostado',
        df_tostion_hoja2.columns[9]: 'Perfil',
        df_tostion_hoja2.columns[10]: 'Temp_Inicio_Final',
        df_tostion_hoja2.columns[11]: 'Tiempo_Tueste',
        df_tostion_hoja2.columns[12]: 'Observaciones_Tostion',
        df_tostion_hoja2.columns[13]: 'Tostador'
    }, inplace=True)

    # df_despachos_second
    df_despachos_hoja2.rename(columns={
        df_despachos_hoja2.columns[0]: 'Pedido',
        df_despachos_hoja2.columns[1]: 'Fecha_Tueste_Despacho',
        df_despachos_hoja2.columns[2]: 'Fecha_Empaque',
        df_despachos_hoja2.columns[3]: 'Tipo_Cafe',
        df_despachos_hoja2.columns[4]: 'Presentacion',
        df_despachos_hoja2.columns[5]: 'NaN_Col1',
        df_despachos_hoja2.columns[6]: 'Cantidad_Despacho',
        df_despachos_hoja2.columns[7]: 'NaN_Col2',
        df_despachos_hoja2.columns[8]: 'NaN_Col3',
        df_despachos_hoja2.columns[9]: 'Cliente',
        df_despachos_hoja2.columns[10]: 'Responsable_Despacho',
        df_despachos_hoja2.columns[11]: 'Verifica'
    }, inplace=True)

    # Concatenar los DataFrames de las hojas principales y secundarias
    df_calidad = pd.concat([df_calidad_hoja1, df_calidad_hoja2], ignore_index=True)
    df_tostion = pd.concat([df_tostion_hoja1, df_tostion_hoja2], ignore_index=True)
    df_despachos = pd.concat([df_despachos_hoja1, df_despachos_hoja2], ignore_index=True)

    # Convertir 'Puntaje_Taza' a numérico en df_calidad
    df_calidad['Puntaje_Taza'] = pd.to_numeric(df_calidad['Puntaje_Taza'], errors='coerce')

    # Unir df_calidad y df_tostion por Lote
    df_merged = pd.merge(df_calidad, df_tostion, left_on='Lote_Calidad', right_on='Lote_Tostion', how='inner', suffixes=('_calidad', '_tostion'))

    return df_merged

if __name__ == "__main__":
    print(data_merged())

