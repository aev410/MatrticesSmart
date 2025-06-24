import pandas as pd
import pytest
from filtrado import leer_archivo, separar_columnas
from pandas.testing import assert_frame_equal

COLUMNAS = [
    "Marca temporal", "Dirección de correo electrónico", "Pregunta 1 [Importancia]", 
    "Pregunta 1 [Urgencia]", "Pregunta 1 [Esfuerzo organizativo]", "Pregunta 1 [Impacto]",
    "Pregunta 2 [Importancia]", "Pregunta 2 [Urgencia]", "Pregunta 2 [Esfuerzo organizativo]", 
    "Pregunta 2 [Impacto]", "Pregunta 3 (respuesta abierta)", "Pregunta 4 [Importancia]", 
    "Pregunta 4 [Urgencia]", "Pregunta 4 [Esfuerzo organizativo]", "Pregunta 4 [Impacto]",
    "Pregunta 5 (sí/no)", "Pregunta 6 (respuesta abierta)", "Pregunta 7 [Importancia]",
    "Pregunta 7 [Urgencia]", "Pregunta 7 [Esfuerzo organizativo]", "Pregunta 7 [Impacto]",
    "Pregunta 8 (respuesta abierta)", "Pregunta 9 [Importancia]", "Pregunta 9 [Urgencia]", 
    "Pregunta 9 [Esfuerzo organizativo]", "Pregunta 9 [Impacto]", "Pregunta 10 [Importancia]",
    "Pregunta 10 [Urgencia]", "Pregunta 10 [Esfuerzo organizativo]", "Pregunta 10 [Impacto]",
    "Pregunta 11 [Importancia]", "Pregunta 11 [Urgencia]", "Pregunta 11 [Esfuerzo organizativo]",
    "Pregunta 11 [Impacto]", "Pregunta 12 [Alimentación]", "Pregunta 12 [Comportamiento de los menores]",
    "Pregunta 12 [Actividades en tiempo libre]", "Pregunta 12 [Limpieza e higiene]",
    "Pregunta 12 [Capacidad de los monitores]", "Pregunta 13 [Importancia]", "Pregunta 13 [Urgencia]",
    "Pregunta 13 [Esfuerzo organizativo]", "Pregunta 13 [Impacto]", "Pregunta 14 [Importancia]",
    "Pregunta 14 [Urgencia]", "Pregunta 14 [Esfuerzo organizativo]", "Pregunta 14 [Impacto]",
    "Observaciones y aportaciones"
]

@pytest.mark.parametrize("extension", [".xlsx", ".csv", ".ods"])
def test_leer_archivo_formatos_y_contenido(tmp_path, extension):
    archivo_path = tmp_path / f"archivo_prueba{extension}"
    
    # Creamos un DataFrame con una fila de datos de ejemplo
    df_original = pd.DataFrame([[
        "2025-01-01 10:00:00", "usuario@example.com", 5, 4, 3, 2,
        5, 4, 3, 2, "Texto libre", 4, 4, 3, 2,
        "Sí", "Otro texto", 5, 4, 3, 2,
        "Otra respuesta", 5, 4, 3, 2, 5, 4, 3, 2,
        5, 4, 3, 2, "Bien", "Adecuado", "Suficiente", "Limpio", "Capacitado",
        4, 3, 2, 1, 4, 3, 2, 1, "Todo bien"
    ]], columns=COLUMNAS)

    # Guardamos el archivo
    if extension == ".xlsx":
        df_original.to_excel(archivo_path, index=False, engine="openpyxl")
    elif extension == ".csv":
        df_original.to_csv(archivo_path, index=False)
    elif extension == ".ods":
        df_original.to_excel(archivo_path, index=False, engine="odf")

    # Leer con la función
    resultado = leer_archivo(str(archivo_path))

    # Validaciones
    assert isinstance(resultado, pd.DataFrame)
    assert list(resultado.columns) == COLUMNAS
    assert_frame_equal(resultado, df_original, check_dtype=False)



def test_separar_columnas():
    columnas = [
        "Pregunta 1 [Importancia]",
        "Pregunta 1 [Urgencia]",
        "Pregunta 1 [Esfuerzo organizativo]",
        "Pregunta 1 [Impacto]",
        "Pregunta abierta",
        "Observaciones",
        "Email",
    ]

    df = pd.DataFrame(columns=columnas)

    columnas_matriz, columnas_fuera_matriz = separar_columnas(df)

    # Esperados
    esperadas_matriz = [
        "Pregunta 1 [Importancia]",
        "Pregunta 1 [Urgencia]",
        "Pregunta 1 [Esfuerzo organizativo]",
        "Pregunta 1 [Impacto]",
    ]

    esperadas_fuera = [
        "Pregunta abierta",
        "Observaciones",
        "Email",
    ]

    assert set(columnas_matriz) == set(esperadas_matriz)
    assert set(columnas_fuera_matriz) == set(esperadas_fuera)