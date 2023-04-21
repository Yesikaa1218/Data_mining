import os
import shutil
import pandas as pd


os.environ['KAGGLE_USERNAME'] = 'yesicaventura'
os.environ['KAGGLE_KEY'] = 'e98ce10effb734b46006c62914fc5ecd'

from kaggle.api.kaggle_api_extended import KaggleApi

dataset = 'kamilpytlak/personal-key-indicators-of-heart-disease'
path = 'heart_2020'

print("\t\tPRACTICA #1 --> ADQUISICIÓN DE DATOS\n\n")
print ("Descarga del archivo a la carpeta llamada heart_2020")

api = KaggleApi()
api.authenticate()

api.dataset_download_files(dataset, path)

shutil.unpack_archive('heart_2020/personal-key-indicators-of-heart-disease.zip', path)
os.remove("heart_2020/personal-key-indicators-of-heart-disease.zip")
print ("Descarga exitosa, procede a la lectura del archivo: ")

data = pd.read_csv('heart_2020_cleaned.csv')

# visualizar las primeras filas del DataFrame
print(data.head(1000))