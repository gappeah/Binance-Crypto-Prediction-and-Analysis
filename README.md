Cryptocurrency Price Prediction with LSTM

This project uses an LSTM (Long Short-Term Memory) model to predict cryptocurrency prices.

Key Features:

    Fetches cryptocurrency data from the CoinMarketCap API
    Normalizes the dataset using MinMaxScaler
    Splits the dataset into training and testing sets
    Builds an LSTM model with PyTorch
    Trains the model using mean squared error (MSE) loss
    Evaluates the model's performance using root mean squared error (RMSE)
    Visualizes the actual vs. predicted prices

Prerequisites:

    Python 3.x
    Required libraries: requests, pandas, numpy, matplotlib, sklearn, torch
    A CoinMarketCap API key (replace YOUR_API_KEY in the code)

Instructions:

    Clone or download this repository.
    Install the required libraries: pip install -r requirements.txt
    Replace YOUR_API_KEY in the code with your actual CoinMarketCap API key.
    Run the Python script: python main.py

Output:

    The script will print the training loss and RMSE for each epoch.
    It will also generate a plot comparing the actual vs. predicted prices.

Additional Notes:

    The current model is designed for Bitcoin (BTC) predictions. You can modify the crypto_symbol variable to predict prices for other cryptocurrencies.
    The model uses a simple dataset for demonstration purposes. Consider using more extensive historical data for real-world applications.
