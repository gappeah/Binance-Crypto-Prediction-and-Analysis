import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch.autograd import Variable
from sklearn.metrics import mean_squared_error

# Function to collect cryptocurrency data from CoinMarketCap API
def get_crypto_data(symbol):
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': symbol, 'convert': 'USD'}
    headers = {'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    price = data['data'][symbol]['quote']['USD']['price']
    return price

# Function to create dataset for LSTM
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return np.array(dataX), np.array(dataY)

# Specify the cryptocurrency you want to predict
crypto_symbol = 'BTC'

# Collect historical cryptocurrency data (use your data source)
# In this example, we'll create a simple dataset
data = pd.DataFrame({'Price': np.random.rand(1000) * get_crypto_data(crypto_symbol)})

# Normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
data['Price'] = scaler.fit_transform(data['Price'].values.reshape(-1, 1))

# Split the dataset into training and testing sets
train_size = int(len(data) * 0.67)
test_size = len(data) - train_size
train, test = data[0:train_size], data[train_size:len(data)]

# Create dataset for LSTM
look_back = 1
trainX, trainY = create_dataset(train['Price'], look_back)
testX, testY = create_dataset(test['Price'], look_back)

# Convert to PyTorch tensors
trainX = torch.from_numpy(trainX).type(torch.FloatTensor)
trainY = torch.from_numpy(trainY).type(torch.FloatTensor)
testX = torch.from_numpy(testX).type(torch.FloatTensor)
testY = torch.from_numpy(testY).type(torch.FloatTensor)

# Build the LSTM model
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTM, self).__init()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

input_size = 1
hidden_size = 64
num_layers = 1
output_size = 1
model = LSTM(input_size, hidden_size, num_layers, output_size)

# Loss and optimizer
criterion = nn.MSELoss()
learning_rate = 0.001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training the model
num_epochs = 100
for epoch in range(num_epochs):
    outputs = model(trainX)
    optimizer.zero_grad()
    loss = criterion(outputs, trainY)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Test the model
model.eval()
test_predict = model(testX)

# Inverse transform the predictions to the original scale
test_predict = scaler.inverse_transform(test_predict.data.numpy())
testY = scaler.inverse_transform(testY.data.numpy())

# Calculate root mean squared error
rmse = np.sqrt(mean_squared_error(testY, test_predict))
print(f'Root Mean Squared Error: {rmse:.4f}')

# Plot the actual vs. predicted prices
plt.plot(data.index[train_size + look_back:], testY, label='Actual')
plt.plot(data.index[train_size + look_back:], test_predict, label='Predicted')
plt.legend()
plt.show()
