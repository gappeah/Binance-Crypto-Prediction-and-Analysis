# Binance Crypto Prediction and Analysis

This project demonstrates how to connect to the Binance API, retrieve real-time data for Bitcoin (BTC) and Ethereum (ETH), perform data preprocessing and visualization, and create a predictive model using Long Short-Term Memory (LSTM) neural networks. [Based on this tutorial](https://heartbeat.comet.ml/analyzing-and-creating-a-predictive-model-for-binance-data-69171dbd5bec "Based on this tutorial")

![output_1](https://github.com/user-attachments/assets/61a5e7c6-5240-4ad2-959d-2aa712490aa5)
![output_2](https://github.com/user-attachments/assets/d06e7cab-9fe7-4961-8314-08b07bfb9207)
![output](https://github.com/user-attachments/assets/6e18ff07-a8a2-4486-872e-1a8af86f3d21)

# What is Bitcoin

Bitcoin is a decentralised digital currency that was introduced in 2009 by an anonymous person or group using the pseudonym Satoshi Nakamoto. It operates on a peer-to-peer network and utilizes blockchain technology to enable secure, transparent, and immutable transactions without the need for intermediaries like banks.

## Technical Overview

### Blockchain Architecture
Bitcoin's blockchain is a distributed ledger that records all transactions across a network of computers (nodes). Each block in the chain contains a list of transactions, a timestamp, and a cryptographic hash of the previous block, ensuring that the data is securely linked. This structure prevents tampering, as altering any block would require changing all subsequent blocks, which is computationally infeasible due to the consensus mechanisms in place

### Consensus Mechanism
Bitcoin employs a Proof-of-Work (PoW) consensus mechanism, where miners compete to solve complex mathematical problems to validate transactions and create new blocks. The first miner to solve the problem gets to add the new block to the blockchain and is rewarded with newly minted bitcoins and transaction fees. This process requires significant computational power and energy consumption, which has raised environmental concerns.

### Transaction Process
When a user initiates a transaction, it is broadcasted to the network. Miners collect these transactions into a block. Once a block is filled, miners work on solving the PoW problem. Upon successful validation, the new block is added to the blockchain, and the transaction becomes irreversible. Bitcoin transactions are recorded in a public ledger accessible to anyone, enhancing transparency while maintaining user anonymity through cryptographic addresses.

### Security Features
Bitcoin's security relies heavily on cryptographic techniques:
- **Hash Functions**: Bitcoin uses SHA-256 as its hashing algorithm. Each block's hash is generated based on its contents and the hash of the previous block, creating an unbreakable chain.
- **Digital Signatures**: Transactions are signed using private keys associated with Bitcoin addresses. This ensures that only the owner of an address can authorize spending their bitcoins.
- **Decentralization**: The lack of central authority means that no single entity can control or manipulate the network. This decentralization contributes to its security and resistance against censorship[4][5].

## Use Cases
Bitcoin primarily serves as a digital currency for peer-to-peer transactions but has also been adopted for various applications:
- **Store of Value**: Often referred to as "digital gold," Bitcoin is used as a hedge against inflation and economic instability.
- **Remittances**: Bitcoin allows for low-cost cross-border transactions without relying on traditional banking systems.
- **Investment**: Many investors view Bitcoin as an asset class, contributing to its growing popularity among retail and institutional investors alike.
  
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
- [NumPy](https://numpy.org/) -  A library that adds support for large, multi-dimensional arrays and matrices
- [Pandas](https://pandas.pydata.org/) - A fast, powerful, flexible and easy to use open source data analysis for manipulating datasets
