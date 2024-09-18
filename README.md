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
When a user initiates a transaction, it is broadcast to the network. Miners collect these transactions into a block. Once a block is filled, miners work on solving the PoW problem. Upon successful validation, the new block is added to the blockchain, and the transaction becomes irreversible. Bitcoin transactions are recorded in a public ledger accessible to anyone, enhancing transparency while maintaining user anonymity through cryptographic addresses.

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

## What is Ethereum 
Ethereum is a decentralised, global platform that uses blockchain technology to enable the creation of digital applications and currencies. It's known for its native cryptocurrency, ether (ETH) and is often mentioned alongside Bitcoin as a leader in the cryptocurrency and blockchain space. 
Ethereum is a decentralized, open-source blockchain platform that enables developers to build and deploy decentralized applications (DApps) through the use of smart contracts. It was proposed by Vitalik Buterin in 2013 and officially launched on July 30, 2015. The native cryptocurrency of the Ethereum network is Ether (ETH), which serves multiple purposes, including transaction fees and as a means of value transfer.

### Blockchain Architecture
Ethereum operates on a blockchain, which is a distributed ledger technology that records transactions in a secure and immutable manner. Each block in the Ethereum blockchain contains a cryptographic hash of the previous block, creating a chain that ensures data integrity. This architecture allows for a decentralized network where no single entity has control over the entire blockchain.

### Smart Contracts
Smart contracts are self-executing contracts with the terms directly written into code. They run on the Ethereum Virtual Machine (EVM), which allows any code compatible with EVM to execute on the Ethereum network. Smart contracts facilitate, verify, or enforce the negotiation or performance of a contract without intermediaries, thus reducing costs and increasing efficiency.

### Ethereum Virtual Machine (EVM)
The EVM is a runtime environment for executing smart contracts and DApps on the Ethereum blockchain. It abstracts the underlying complexity of the network, allowing developers to write code in various programming languages that can be compiled into EVM bytecode. The EVM operates in a deterministic manner, ensuring that all nodes reach a consensus on the state of the blockchain after executing transactions.

### Consensus Mechanism
Ethereum transitioned from a Proof-of-Work (PoW) to a Proof-of-Stake (PoS) consensus mechanism with an upgrade known as "the Merge" on September 15, 2022. In PoS, validators are chosen to create new blocks based on the amount of ETH they hold and are willing to "stake" as collateral. This shift significantly reduced Ethereum's energy consumption by approximately 99% compared to its previous mining model.

### Gas Fees
Transactions on the Ethereum network require gas fees, which are paid in ETH. Gas serves as a measure of computational effort required to execute operations like transactions and smart contract executions. The fee structure incentivizes miners/validators to process transactions and prevents spam attacks on the network by requiring users to pay for resources consumed.

### Use Cases
Ethereum supports various applications across multiple domains:
- **Decentralized Finance (DeFi)**: Platforms built on Ethereum allow users to lend, borrow, trade, and earn interest without traditional financial intermediaries.
- **Non-Fungible Tokens (NFTs)**: Ethereum provides a framework for creating unique digital assets that represent ownership of specific items or content.
- **Decentralized Autonomous Organizations (DAOs)**: These entities operate through smart contracts, allowing members to govern collectively without centralized control.
  
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
