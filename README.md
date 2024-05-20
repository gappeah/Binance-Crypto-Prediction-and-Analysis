# ETH To BTC Prediction And Analysis Model

This project demonstrates how to connect to the Binance API, retrieve real-time data for Bitcoin (BTC) and Ethereum (ETH), perform data preprocessing and visualization, and create a predictive model using Long Short-Term Memory (LSTM) neural networks. [Based on this tutorial](https://heartbeat.comet.ml/analyzing-and-creating-a-predictive-model-for-binance-data-69171dbd5bec "Based on this tutorial")

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- Anaconda
- Binance account (to obtain API key and secret)
- Jupyter Notebook
- Note: if you are having difficulties with installing Jupytyer Notebook on Visual Code Studio I recommend you watch [this video](https://www.youtube.com/watch?v=h1sAzPojKMg) which explains how to set up Jupytyer Notebook and Anaconda in less than 4 minutes.


## Installation

1. Clone the repository:

```
git clone https://github.com/gappeah/Binance-Crypto-Prediction-and-Analysis.git
```

2. Navigate to the project directory:

```
cd Binance-Crypto-Prediction-and-Analysis
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

4. Create a `config.ini` file in the project directory with your Binance API key and secret:

```ini
[binance]
api_key = your_api_key
api_secret = your_api_secret
```

## Usage

1. Open the `binance_prediction.ipynb` Jupyter Notebook file.

2. Run the notebook cells sequentially to execute the following steps:

   - Import necessary libraries
   - Configure and authenticate with the Binance API
   - Retrieve and preprocess historical data for BTC and ETH
   - Visualize the data using mplfinance
   - Create an LSTM predictive model
   - Test the model on a separate dataset
   - Plot the actual and predicted prices

## Files

- `binance_prediction.ipynb`: Jupyter Notebook containing the main code
- `config.ini`: Configuration file for storing Binance API key and secret (excluded from the repository)
- `requirements.txt`: List of required Python packages

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


## Acknowledgments

- [Python-Binance](https://python-binance.readthedocs.io/en/latest/) - The official Python library for the Binance API
- [mplfinance](https://github.com/matplotlib/mplfinance) - Financial data visualization library for Python
- [TensorFlow](https://www.tensorflow.org/) - Open-source machine learning framework
- [Keras](https://keras.io/) - High-level neural networks API
- [Anaconda](https://www.anaconda.com/) - Distribution of the Python and R 
```
