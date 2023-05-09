import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv('sales_data_sample.csv', encoding='latin-1')

df_before_2004 = df.loc[df['YEAR_ID'] < 2004]
df_after_2004 = df.loc[df['YEAR_ID'] >= 2004]

# Aquí calculamos la promedio de las ventas
mean_before_2004 = df_before_2004['SALES'].mean()
mean_after_2004 = df_after_2004['SALES'].mean()

# Prueba t
t, p = stats.ttest_ind(df_before_2004['SALES'].dropna(), df_after_2004['SALES'].dropna())

fig, ax = plt.subplots()
sns.barplot(x=['Before 2004', 'After 2004'], y=[mean_before_2004, mean_after_2004], ax=ax)
ax.set_ylabel('Promedio de Ventas')
ax.set_title('Comparación antes de 2004 y después')
plt.show()
plt.savefig('2004.png')


fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(['t', 'p'], [t, p], color=['blue', 'red'])
plt.title('Resultado de la prueba estadística')
plt.ylabel('Valor')
plt.show()
plt.savefig('2004_a.png')


