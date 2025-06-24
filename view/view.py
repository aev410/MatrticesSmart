import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from analisis_datos.filtrado import leer_archivo, separar_columnas

def crear_grafico(values: list[tuple[str, pd.DataFrame, pd.DataFrame]]) -> plt.Figure:
    """
    Crea un gráfico de dispersión con líneas de referencia en el eje x e y.
    Args:
        values (list[tuple[str, pd.DataFrame, pd.DataFrame]]): Lista de tuplas que contienen el nombre del punto y las columnas de datos para el eje x e y.
    Returns:
        plt.Figure: Figura de matplotlib con el gráfico de dispersión.
    
    """ 
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    ax.axhline(y=2.5, color='gray', linestyle='--')
    ax.axvline(x=2.5, color='gray', linestyle='--')
    
    for nombre, col1, col2 in values:
        x = col1
        y = col2
        ax.scatter(x, y, label=nombre, color='blue')
        ax.text(x + 0.05, y, nombre, fontsize=9)
        
    ax.grid(True, linestyle='--', alpha=0.5)
    
    return fig

if __name__ == "__main__":
    
    ruta = '../test/data/datos.xlsx'
    df = leer_archivo(ruta)
    columnas_matriz, columnas_fuera_matriz = separar_columnas(df)
    importacia_urgencia, esfuerzo_impacto = separar_columnas(df, patrones=['\[Importancia\]', '\[Urgencia\]'])
    
    
    st.pyplot(crear_grafico())