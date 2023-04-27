import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import f_oneway


df = pd.read_csv('games.csv')


df_before_2020 = df.loc[df['Release Date'] < 'Jan 1, 2020']
df_after_2020 = df.loc[df['Release Date'] >= 'Jan 1, 2020']

#Aquí calculamos la calificación promedio
mean_before_2020 = df_before_2020['Rating'].mean()
mean_after_2020 = df_after_2020['Rating'].mean()

#Prueba t
t, p = stats.ttest_ind(df_before_2020['Rating'].dropna(), df_after_2020['Rating'].dropna())


fig, ax = plt.subplots()
sns.barplot(x=['Before 2020', 'After 2020'], y=[mean_before_2020, mean_after_2020], ax=ax)
ax.set_ylabel('Promedio')
ax.set_title('Comparación antes del 2020 y después.')
plt.show()


fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(['t', 'p'], [t, p], color=['blue', 'red'])

plt.title('Resultado de la prueba estadística')
plt.ylabel('Valor')
plt.show()

