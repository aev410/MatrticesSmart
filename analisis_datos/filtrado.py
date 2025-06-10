import pandas as pd
import os


def leer_archivo(archivo_path):
    ext = os.path.splitext(archivo_path)[1].lower() # Obtener la extensión del archivo
    
    if ext in ['.xlsx', '.xls']:
        return pd.read_excel(archivo_path, engine='openpyxl') # Necesita `openpyxl`
    elif ext == '.csv':
        return pd.read_csv(archivo_path)
    elif ext == '.ods':
        return pd.read_excel(archivo_path, engine='odf')  # Necesita `odfpy` instalado
    else:
        raise ValueError("Formato de archivo no soportado")




if __name__ == "__main__":
    ruta = 'MatrticesSmart/excel/Respuestas_linea5.xlsx'
    df = leer_archivo(ruta)