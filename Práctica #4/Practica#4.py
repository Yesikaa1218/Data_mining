import pandas as pd
import matplotlib.pyplot as plt

#Práctica 4
df = pd.read_csv('heart_2020_cleaned.csv')

#Edad
plt.hist(df['AgeCategory'], bins=20)
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()
plt.savefig('Edad')

#Sexo
Sex_counts = df['Sex'].value_counts()
plt.bar(Sex_counts.index, Sex_counts.values, color='blue')
plt.xlabel('Sexo')
plt.ylabel('Count')
plt.xticks([0, 1], ['Female', 'Male'])
plt.show()
plt.savefig('sex.png')

#Enfermedades cardiacas
target_counts = df['HeartDisease'].value_counts()
labels = ['Sin enfermedad cardiaca', 'Enfermedad Cardiaca']
plt.pie(target_counts.values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.savefig('enfermedad_cardiaca.png')

#Gráfico de dispersión en relación de la edad y el tiempo de sueño
plt.scatter(df['AgeCategory'], df['SleepTime'])
plt.xlabel('Edad')
plt.ylabel('Horas de sueño')
plt.show()
plt.savefig('dispersion_sueño.png')

#Edad y salud mental
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].hist(df['AgeCategory'], bins=20)
ax[0].set_xlabel('Edad')
ax[0].set_ylabel('Frecuencia')
ax[0].set_title('Distribución por edad')
ax[1].hist(df['MentalHealth'], bins=20)
ax[1].set_xlabel('Salud mental')
ax[1].set_ylabel('Frecuencia')
ax[1].set_title('Distribución de Salud mental')
plt.show()
plt.savefig('histograma_salud_Edad.png')


#Gráfica circular de Alcohol y Fumadores

target_counts = df['Smoking'].value_counts()
labels = ['Fumadores', 'No fumadores']
colors = ['lightcoral', 'lightskyblue']
plt.pie(target_counts.values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.savefig('Fumadores.png')


target_counts = df['AlcoholDrinking'].value_counts()
labels = ['Alcohólicos', 'No Alcohólicos']
colors = ['lightgreen', 'lightskyblue']
plt.pie(target_counts.values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.savefig('Alcohol.png')
