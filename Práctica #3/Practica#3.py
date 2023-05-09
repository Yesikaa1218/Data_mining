import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data_sample.csv', encoding='latin-1')
# Calcular estadísticas descriptivas
print(df.describe())

# Precio y volumen de ventas por mes
df['MONTH_ID'] = pd.to_datetime(df['MONTH_ID'])
df_monthly = df.groupby(df['MONTH_ID'].dt.strftime('%Y-%m')).sum(numeric_only=True)

plt.plot(df_monthly.index, df_monthly['SALES'], label='Ventas')
plt.plot(df_monthly.index, df_monthly['PRICEEACH'], label='Precio')
plt.title('Ventas y precio por mes')
plt.xlabel('Mes')
plt.ylabel('Valor')
plt.legend()
plt.show()

# Cantidad de ventas por línea de producto
product_line_counts = df['PRODUCTLINE'].value_counts()

plt.bar(product_line_counts.index, product_line_counts.values)
plt.title('Cantidad de ventas por línea de producto')
plt.xlabel('Línea de producto')
plt.ylabel('Cantidad de ventas')
plt.xticks(rotation=45)
plt.show()
