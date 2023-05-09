import pandas as pd
import matplotlib.pyplot as plt

# Práctica 4
df = pd.read_csv('sales_data_sample.csv', encoding='latin-1')


plt.hist(df['YEAR_ID'], bins=20)
plt.xlabel('Año')
plt.ylabel('Frecuencia')
plt.show()
plt.savefig('Año.png')

sex_counts = df['PRODUCTLINE'].value_counts()
plt.bar(sex_counts.index, sex_counts.values, color='blue')
plt.xlabel('Línea de producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=90)
plt.show()
plt.savefig('Linea_producto.png')


target_counts = df['STATUS'].value_counts()
labels = ['En proceso', 'Completado']
labels = target_counts.index.tolist()
plt.pie(target_counts.values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.savefig('Estado_pedido.png')

# Gráfico de dispersión en relación del precio y la cantidad ordenada
plt.scatter(df['PRICEEACH'], df['QUANTITYORDERED'])
plt.xlabel('Precio')
plt.ylabel('Cantidad ordenada')
plt.show()
plt.savefig('dispersion_precio_cantidad.png')


fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].hist(df['MSRP'], bins=20)
ax[0].set_xlabel('Precio sugerido por el fabricante')
ax[0].set_ylabel('Frecuencia')
ax[0].set_title('Distribución de precios')
ax[1].hist(df['SALES'], bins=20)
ax[1].set_xlabel('Ventas')
ax[1].set_ylabel('Frecuencia')
ax[1].set_title('Distribución de ventas')
plt.show()
plt.savefig('histograma_precio_ventas.png')


target_counts = df['COUNTRY'].value_counts()
labels = target_counts.index.tolist()
plt.pie(target_counts.values, labels=labels, autopct='%1.1f%%')

plt.axis('equal')
plt.show()
plt.savefig('Distribucion_paises.png')

target_counts = df['DEALSIZE'].value_counts()
labels = target_counts.index
plt.pie(target_counts.values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.savefig('Tamaño_negocio.png')
