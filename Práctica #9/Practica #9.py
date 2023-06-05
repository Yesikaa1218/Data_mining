import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering


data = pd.read_csv('sales_data_sample.csv', encoding='latin-1')


features = ['QUANTITYORDERED', 'PRICEEACH', 'SALES']


X = data[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_


data['Cluster'] = labels

#Gráfico de dispersión
plt.scatter(data['QUANTITYORDERED'], data['PRICEEACH'], c=data['Cluster'])
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=100)
plt.xlabel('Quantity Ordered')
plt.ylabel('Price Each')
plt.title('Sales Data Clustering')
plt.savefig('clustering.jpg')
plt.show()

features = ['QUANTITYORDERED', 'PRICEEACH', 'SALES']


X = data[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


clustering = AgglomerativeClustering(n_clusters=3)
clustering.fit(X_scaled)


labels = clustering.labels_


data['Cluster'] = labels

# gráfico de dispersión
plt.scatter(data['QUANTITYORDERED'], data['PRICEEACH'], c=data['Cluster'])
plt.xlabel('Quantity Ordered')
plt.ylabel('Price Each')
plt.title('Sales Data Clustering')
plt.savefig('clustering_plot.jpg')
plt.show()