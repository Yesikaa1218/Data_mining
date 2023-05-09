import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


df = pd.read_csv('sales_data_sample.csv', index_col='ORDERDATE', parse_dates=True, encoding='latin1')
y = df['SALES']

train_len = int(len(y) * 0.8)
train = y[:train_len]
test = y[train_len:]

model = SARIMAX(train, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0), trend='c')
model_fit = model.fit()

# Predicciones
preds = model_fit.forecast(steps=len(test))

mse = np.mean((test.values - preds.values) ** 2)

# Impresión gráfica de las predicciones
plt.plot(train.index, train, label='Entrenamiento')
plt.plot(test.index, test, label='Prueba')
plt.plot(test.index, preds, label='Predicciones')
plt.legend()
plt.show()
plt.savefig('prueba1.png')

# Segundo ejemplo
y_norm = (y - y.mean()) / y.std()
seq_len = 30
seqs = []
targets = []
for i in range(seq_len, len(y_norm)):
    seqs.append(y_norm[i - seq_len:i])
    targets.append(y_norm[i])
seqs = np.array(seqs)
targets = np.array(targets)

train_len = int(len(seqs) * 0.8)
train_seqs = seqs[:train_len]
train_targets = targets[:train_len]
test_seqs = seqs[train_len:]
test_targets = targets[train_len:]

model = Sequential()
model.add(LSTM(64, input_shape=(seq_len, 1)))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

history = model.fit(train_seqs.reshape(-1, seq_len, 1), train_targets, epochs=50, batch_size=32, verbose=2,
                    validation_data=(test_seqs.reshape(-1, seq_len, 1), test_targets))

preds = model.predict(test_seqs.reshape(-1, seq_len, 1)).squeeze()

preds = preds * y.std() + y.mean()
test_targets = test_targets * y.std() + y.mean()

mse = np.mean((test_targets - preds) ** 2)

# Impresión gráfica de las predicciones
plt.plot(df.index[train_len + seq_len:], test_targets, label='Prueba')
plt.plot(df.index[train_len + seq_len:], preds, label='Predicciones')
plt.legend()
plt.show()
plt.savefig('prueba2.png')
