import os
import shutil
import pandas as pd


os.environ['KAGGLE_USERNAME'] = 'yesicaventura'
os.environ['KAGGLE_KEY'] = 'e98ce10effb734b46006c62914fc5ecd'

from kaggle.api.kaggle_api_extended import KaggleApi

dataset = 'ankitchahal1/sales-data'
path = 'sales_data'

print("\t\tPRACTICA #1 --> ADQUISICIÓN DE DATOS\n\n")
print("Descargando el archivo a la carpeta llamada sales_data")

# Autenticar y descargar el conjunto de datos
api = KaggleApi()
api.authenticate()
api.dataset_download_files(dataset, path)

# Descomprimir el archivo descargado
shutil.unpack_archive('sales_data/sales-data.zip', path)
os.remove("sales_data/sales-data.zip")

print("Descarga exitosa, procediendo a la lectura del archivo:")

# Leer el archivo CSV
data = pd.read_csv('sales_data/SalesDataSample.csv', encoding='latin1')

# Visualizar las primeras filas del DataFrame
print(data.head(1000))
