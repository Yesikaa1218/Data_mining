import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('games.csv')

df['Plays'] = df['Plays'].str.replace('K', '000').astype(float)
df['Number of Reviews'] = df['Number of Reviews'].str.replace('K', '000').astype(float)


X = df[['Number of Reviews']]
y = df[['Plays']]

model = LinearRegression()
model.fit(X, y)

print('Coeficiente:', model.coef_[0])
print('Intercepción:', model.intercept_)

plt.scatter(X, y)

X_test = pd.DataFrame({'Number of Reviews': range(5000)})
y_pred = model.predict(X_test)

# línea de regresión
plt.plot(X_test, y_pred, color='red')
plt.show()




