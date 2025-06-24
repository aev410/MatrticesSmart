import pandas as pd
import os
import re


def leer_archivo(archivo_path:  str) -> pd.DataFrame:
    """
    Lee un archivo de Excel, CSV u ODS y devuelve un DataFrame de pandas.

    Args:
        archivo_path (str): Ruta al archivo a leer.

    Raises:
        ValueError: Si el formato del archivo no es soportado.

    Returns:
        pd.DataFrame: DataFrame con los datos del archivo leído.
    """
    # Obtener la extensión del archivo
    ext = os.path.splitext(archivo_path)[1].lower()

    if ext in ['.xlsx', '.xls']:
        # Necesita `openpyxl`
        return pd.read_excel(archivo_path, engine='openpyxl')
    elif ext == '.csv':
        return pd.read_csv(archivo_path)
    elif ext == '.ods':
        # Necesita `odfpy` instalado
        return pd.read_excel(archivo_path, engine='odf')
    else:
        raise ValueError("Formato de archivo no soportado")


def separar_columnas(df:  pd.DataFrame, patrones = ['\[Importancia\]', '\[Urgencia\]', '\[Esfuerzo organizativo\]', '\[Impacto\]']) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Separa las columnas de un DataFrame en dos grupos: aquellas que contienen patrones específicos
    y aquellas que no.
    Patrones:
        - Importancia
        - Urgencia
        - Esfuerzo organizativo
        - Impacto
    Estos patrones se buscan en los nombres de las columnas.
    Args:
        df (pd.DataFrame): DataFrame a procesar.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: columnas que cumplen los patrones y columnas que no cumplen los patrones.
    """    
    
    # patrones = ['\[Importancia\]', '\[Urgencia\]', '\[Esfuerzo organizativo\]', '\[Impacto\]']

    columnas_matriz = []
    columnas_fuera_matriz = []

    for col in df.columns:
        if any(re.search(pat, col) for pat in patrones):
            columnas_matriz.append(col)
        else:
            columnas_fuera_matriz.append(col)

    return columnas_matriz, columnas_fuera_matriz

def obtener_datos(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """
    Obtiene los datos de las columnas que cumplen los patrones especificados.

    Args:
        df (pd.DataFrame): DataFrame original.
        columnas_fuera_matriz (list): Lista de nombres de columnas

    Returns:
        pd.DataFrame: DataFrame con las columnas
    """
    return df[columnas]

def media_columna(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """Calcula la media de las columnas especificadas en un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame del que se calculará la media.
        columnas (list): Lista de nombres de columnas para calcular la media.

    Returns:
        pd.DataFrame: DataFrame con la media de las columnas especificadas.
    """
    datos_media = {}
    for col in columnas:
        datos_media[col] = df[col].mean()
        
    datos_media_df = pd.DataFrame(datos_media, index=[0])
    return datos_media_df.reset_index()

if __name__ == "__main__":
    ruta = '../test/data/datos.xlsx'
    df = leer_archivo(ruta)
    print("Columnas originales:", df.columns.tolist())
    columnas_matriz, columnas_fuera_matriz = separar_columnas(df)
    # print("Columnas separadas:")
    # print("Columnas en matriz:", columnas_matriz)
    # print("Columnas fuera de matriz:", columnas_fuera_matriz)
    # print("\n\nDatos sobrantes:")
    # print(obtener_datos(df, columnas_matriz).head())
    
    print("\n\nMedia de las columnas:")
    
    # media_columna(df, columnas_matriz).to_csv('media_columnas.csv', index=False)
    media_col = media_columna(df, columnas_matriz)
    
    print(media_col[columnas_matriz[0]].to_string(index=False))