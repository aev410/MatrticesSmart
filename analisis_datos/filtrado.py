import pandas as pd

ruta = './excel/Linea 5_Promover el acceso a la vivienda. (respuestas).xlsx'
# Lee la primera hoja por defecto
df = pd.read_excel(ruta)

criterios = ["Importancia", "Urgencia", "Esfuerzo organizativo", "Impacto"]

# Seleccionamos solo las columnas que contienen esos criterios
cols_relevantes = [col for col in df.columns if any(c in col for c in criterios)]
df_filtrado = df[cols_relevantes]

escala = {
    "Muy en desacuerdo": 1,
    "En desacuerdo": 2,
    "De acuerdo": 3,
    "Muy de acuerdo": 4,
    "Si": 3,
    "No": 1,
}

# Aplica el mapeo
df_numerico = df_filtrado.replace(escala)

temas = {
    "Viviendas protección oficial": [col for col in df.columns if "viviendas de protección oficial" in col],
    "Vivienda vacía": [col for col in df.columns if "vivienda vacía" in col],
    "Gravar viviendas desocupadas": [col for col in df.columns if "grabar las viviendas desocupadas" in col],
    "Cooperación asociaciones": [col for col in df.columns if "cooperación entre las diferentes asociaciones" in col],
    "Bolsa de viviendas": [col for col in df.columns if "bolsa de viviendas" in col]
}


resultados = {}
for tema, columnas in temas.items():
    puntuacion = df[columnas].replace(escala).mean(axis=1).values[0]  # solo 1 fila
    resultados[tema] = puntuacion


print(resultados)