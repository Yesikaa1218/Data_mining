import pandas as pd


df = pd.read_csv("netflix_titles.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df["type"].value_counts())

print(df.duplicated().sum()) #Verificar si hay dobles
df.drop_duplicates(inplace=True) #Eliminar

print(df.isna().sum()) #Valores faltantes

df["director"].fillna("Desconocido", inplace=True) #Reemplazar

df.dropna(inplace=True)

df.drop(columns=["show_id", "date_added"], inplace=True) #Eliminar columnas no necesarias

df = df[df["duration"].str.contains("min")]

df["duration"] = df["duration"].str.replace(" min", "").astype(int)

def transformar_titulo(titulo):
    return titulo.upper()

df["title"] = df["title"].apply(transformar_titulo)

df.to_csv("netflix_titles_cleaned.csv", index=False)

print("Limpieza realizada con éxito, documento generado: netflix_titles_cleaned")