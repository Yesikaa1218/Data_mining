import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("ifood_df.csv")

# Explorar los datos


# Limpieza de datos básica
df = df.dropna() # Eliminar filas con valores nulos
df = df.drop_duplicates() # Eliminar filas duplicadas


std_dev = df.std()
variances = df.var()
pd.set_option('display.float_format', lambda x: '%.6f' % x)


print("Desviación estándar por cada columna:\n", std_dev)
print("\nVarianza por cada columna:\n", variances)


fig, ax = plt.subplots()
std_dev.plot(kind="bar", ax=ax, color="blue")
ax.set_xlabel("Columnas numéricas")
ax.set_ylabel("Desviación estándar")
ax.set_title("Desviación estándar de cada columna numérica")
plt.show()

# Graficar varianza
fig, ax = plt.subplots()
variances.plot(kind="bar", ax=ax, color="green")
ax.set_xlabel("Columnas numéricas")
ax.set_ylabel("Varianza")
ax.set_title("Varianza de cada columna numérica")
plt.show()

# Graficar dispersión
fig, ax = plt.subplots()
ax.scatter(df["Income"], df["MntTotal"], color="red")
ax.set_xlabel("Income")
ax.set_ylabel("MntTotal")
ax.set_title("Relación entre Income y MntTotal")
plt.show()
