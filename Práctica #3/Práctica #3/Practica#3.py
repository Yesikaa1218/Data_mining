import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('coffee.csv')

# Calcular estadísticas descriptivas
print(df.describe()) #Imprimimos, por lo tanto damos por hecho que el .csv se leyó correctamente

# precio de apertura, cierre, máximo y mínimo por día
plt.plot(df['Date'], df['Open'], label='Apertura')
plt.plot(df['Date'], df['Close'], label='Cierre')
plt.plot(df['Date'], df['High'], label='Máximo')
plt.plot(df['Date'], df['Low'], label='Mínimo')
plt.title('Precio del café por día')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.legend()
plt.show()
plt.savefig('precio_del_Cafe.png')
#volumen de transacciones por día
plt.plot(df['Date'], df['Volume'])
plt.title('Volumen de transacciones por día')
plt.xlabel('Fecha')
plt.ylabel('Volumen')
plt.show()
plt.savefig('vol_transacciones_por_dia.png')

#volumen de transacciones
plt.hist(df['Volume'], bins=20)
plt.title('Histograma del volumen de transacciones')
plt.xlabel('Volumen')
plt.ylabel('Frecuencia')
plt.show()
plt.savefig('volumen_transacciones.png')