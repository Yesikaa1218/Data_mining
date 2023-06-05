import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('sales_data_sample.csv', encoding='latin-1')

df['QUANTITYORDERED'] = df['QUANTITYORDERED'].astype(float)
df['SALES'] = df['SALES'].astype(float)

X = df[['QUANTITYORDERED']]
y = df[['SALES']]

model = LinearRegression()
model.fit(X, y)

print('Coeficiente:', model.coef_[0][0])
print('Intercepción:', model.intercept_[0])

plt.scatter(X, y)

X_test = pd.DataFrame({'QUANTITYORDERED': range(0, 1001)})
y_pred = model.predict(X_test)

plt.plot(X_test, y_pred, color='red')
plt.xlabel('QUANTITYORDERED')
plt.ylabel('SALES')
plt.title('Linear Regression')
plt.show()
