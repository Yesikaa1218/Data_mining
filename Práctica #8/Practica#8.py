import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder



#  leer el conjunto de datos
data = pd.read_csv("citrus.csv")

# x y "y"
X = data[['diameter', 'weight', 'red', 'green', 'blue']]
y = data['name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)


confusion = confusion_matrix(y_test, y_pred)

label_encoder = LabelEncoder()
y_pred_encoded = label_encoder.fit_transform(y_pred)


plt.scatter(X_test['diameter'], X_test['weight'], c=y_pred_encoded)
plt.xlabel('Diámetro')
plt.ylabel('Peso')
plt.title('Clasificación de frutas')
plt.savefig('clasificacion.jpg')
plt.show();
plt.close()

plt.figure(figsize=(8, 6))
plt.imshow(confusion, cmap='Blues')
plt.colorbar()
plt.xticks([0, 1], ['Orange', 'Grapefruit'])
plt.yticks([0, 1], ['Orange', 'Grapefruit'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')

plt.savefig('confusion.jpg')
plt.show();
plt.close()



