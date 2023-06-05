import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np
import matplotlib.dates as mdates



data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

data = data['SALES'].values.reshape(-1, 1)


scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data)


train_size = int(len(data_scaled) * 0.8)
train_data = data_scaled[:train_size]
test_data = data_scaled[train_size:]


sequence_length = 100

X_train, y_train = [], []
for i in range(len(train_data) - sequence_length):
    X_train.append(train_data[i:i+sequence_length])
    y_train.append(train_data[i+sequence_length])
X_train, y_train = np.array(X_train), np.array(y_train)


model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(sequence_length, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=10, batch_size=32)


X_test, y_test = [], []
for i in range(len(test_data) - sequence_length):
    X_test.append(test_data[i:i+sequence_length])
    y_test.append(test_data[i+sequence_length])
X_test, y_test = np.array(X_test), np.array(y_test)
test_predictions = model.predict(X_test)


test_predictions = scaler.inverse_transform(test_predictions)
y_test = scaler.inverse_transform(y_test)

# resultados
plt.figure(figsize=(12, 6))
plt.plot(y_test, label='Actual')
plt.plot(test_predictions, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()


plt.savefig('rnn_sales_prediction.jpeg')
plt.show()

# Ejemplo 2

data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

fig, ax = plt.subplots(figsize=(12, 6))

start_index = train_size + sequence_length
end_index = start_index + len(test_predictions)

dates = pd.to_datetime(data['ORDERDATE'].iloc[start_index:])

dates_train = dates[:len(test_predictions)]


ax.plot(dates_train, test_predictions, label='Train Predictions')

indices = np.arange(start_index, len(data))

ax.plot(dates, data['SALES'].iloc[indices], label='Real Sales')

ax.plot(dates, test_predictions, label='Test Predictions')

date_format = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
plt.xticks(rotation=45)

ax.legend()
plt.title('Sales Prediction')
plt.show()

plt.savefig('sales_prediction.jpeg')
