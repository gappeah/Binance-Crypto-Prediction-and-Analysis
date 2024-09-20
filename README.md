# Binance Crypto Prediction and Analysis

This project demonstrates how to connect to the Binance API, retrieve real-time data for Bitcoin (BTC) and Ethereum (ETH), perform data preprocessing and visualization, and create a predictive model using Long Short-Term Memory (LSTM) neural networks. [Based on this tutorial](https://heartbeat.comet.ml/analyzing-and-creating-a-predictive-model-for-binance-data-69171dbd5bec "Based on this tutorial")

# What is Bitcoin
![Bitcoin svg](https://github.com/user-attachments/assets/521c9760-397a-4829-ad06-181704debe73)

Bitcoin is a decentralised digital currency that was introduced in 2009 by an anonymous person or group using the pseudonym Satoshi Nakamoto. It operates on a peer-to-peer network and utilizes blockchain technology to enable secure, transparent, and immutable transactions without the need for intermediaries like banks.

## Technical Overview
Here’s how you can integrate the Bitcoin code examples into your `README.md` file:

---

## Bitcoin Blockchain Architecture

Bitcoin's blockchain is a distributed ledger that records all transactions across a network of computers (nodes). Each block in the chain contains a list of transactions, a timestamp, and a cryptographic hash of the previous block, ensuring that the data is securely linked. This structure prevents tampering, as altering any block would require changing all subsequent blocks, which is computationally infeasible due to the consensus mechanisms in place.

### Example: Retrieving Block Information from Bitcoin's Blockchain

You can use the following code to retrieve information about a specific block from the Bitcoin blockchain using a public API:

```python
import requests

# Access Bitcoin's blockchain via a public API
block_hash = "0000000000000000000e1f078b14e410ff19e215f50150b90ac89a8d1803e7d8"
url = f"https://blockchain.info/rawblock/{block_hash}"

# Fetch the block information
response = requests.get(url)

if response.status_code == 200:
    block_data = response.json()
    print(f"Block Hash: {block_data['hash']}")
    print(f"Block Height: {block_data['height']}")
    print(f"Number of Transactions: {len(block_data['tx'])}")
else:
    print("Error fetching block data")
```

---

## Consensus Mechanism: Proof-of-Work (PoW)

Bitcoin employs a **Proof-of-Work (PoW)** consensus mechanism, where miners compete to solve complex mathematical problems to validate transactions and create new blocks. The first miner to solve the problem gets to add the new block to the blockchain and is rewarded with newly minted bitcoins and transaction fees. This process requires significant computational power and energy consumption.

### Example: Simulating Bitcoin's Proof-of-Work

The following Python code simulates the Proof-of-Work process by attempting to find a hash that meets a certain difficulty level (leading zeros):

```python
import hashlib
import time

def proof_of_work(prev_hash, transactions, difficulty):
    nonce = 0
    while True:
        block_data = f"{prev_hash}{transactions}{nonce}".encode()
        block_hash = hashlib.sha256(block_data).hexdigest()
        
        # Check if the hash meets the required difficulty
        if block_hash.startswith('0' * difficulty):
            return nonce, block_hash
        nonce += 1

prev_hash = "0000000000000000000e1f078b14e410ff19e215f50150b90ac89a8d1803e7d8"
transactions = "Alice->Bob->2BTC"
difficulty = 5  # Number of leading zeros required in hash

start_time = time.time()
nonce, valid_hash = proof_of_work(prev_hash, transactions, difficulty)
end_time = time.time()

print(f"Valid Hash: {valid_hash}")
print(f"Nonce: {nonce}")
print(f"Time taken: {end_time - start_time} seconds")
```

---

## Transaction Process

When a user initiates a Bitcoin transaction, it is broadcast to the network. Miners collect these transactions into a block, and once the block is validated, it is added to the blockchain.

### Example: Creating a Simple Bitcoin Transaction

Here is how you can create and sign a Bitcoin transaction:

```python
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import COIN

SelectParams('mainnet')

# Create private and public keys
private_key = CBitcoinSecret('YourPrivateKeyHere')
address = P2PKHBitcoinAddress.from_pubkey(private_key.pub)

print(f'Bitcoin Address: {address}')

# In practice, you'd create and broadcast a real transaction through a Bitcoin client.
```

---

## Security Features

Bitcoin's security is based on strong cryptographic techniques such as **hash functions** and **digital signatures**. 

### Hash Functions

Bitcoin uses the **SHA-256** hashing algorithm to secure its blockchain. Each block's hash is generated based on its contents and the hash of the previous block, making the chain immutable.

### Example: Generating a SHA-256 Hash

```python
import hashlib

data = "Hello, Bitcoin!"
hashed_data = hashlib.sha256(data.encode()).hexdigest()

print(f"SHA-256 Hash: {hashed_data}")
```

### Digital Signatures

Bitcoin transactions are signed using private keys. This ensures that only the owner of a Bitcoin address can authorize spending their bitcoins.

### Example: Signing a Message with a Private Key

```python
from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, SignMessage

# Create a private key
private_key = CBitcoinSecret('YourPrivateKeyHere')

# Create a message to sign
message = BitcoinMessage('This is a secure message.')

# Sign the message with the private key
signature = SignMessage(private_key, message)

print(f"Signed Message: {signature}")
```

## What is Ethereum 
![images](https://github.com/user-attachments/assets/9af1cd8b-f9ec-45fb-8e3e-69c382497165)
* Ethereum is a decentralised, global platform that uses blockchain technology to enable the creation of digital applications and currencies.
* It's known for its native cryptocurrency, ether (ETH), and is often mentioned alongside Bitcoin as a leader in the cryptocurrency and blockchain space. 
* Developers can build and deploy decentralised applications (DApps) through the use of smart contracts. It was proposed by Vitalik Buterin in 2013 and officially launched on July 30, 2015.

### Blockchain Architecture
Ethereum operates on a blockchain, which is a distributed ledger technology that records transactions in a secure and immutable manner. Each block in the Ethereum blockchain contains a cryptographic hash of the previous block, creating a chain that ensures data integrity. This architecture allows for a decentralized network where no single entity has control over the entire blockchain.

**Example: Interacting with Ethereum Blockchain to Get the Latest Block**

```python
from web3 import Web3

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Check if connection is successful
if w3.isConnected():
    # Get latest block number
    latest_block = w3.eth.blockNumber
    print(f'Latest block number: {latest_block}')
else:
    print('Failed to connect to Ethereum node')
```

---

### Smart Contracts
Smart contracts are self-executing contracts with the terms directly written into code. They run on the Ethereum Virtual Machine (EVM), which allows any code compatible with EVM to execute on the Ethereum network. Smart contracts facilitate, verify, or enforce the negotiation or performance of a contract without intermediaries, thus reducing costs and increasing efficiency.

**Example: Simple Solidity Smart Contract**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 storedValue;

    // Function to store a value
    function store(uint256 _value) public {
        storedValue = _value;
    }

    // Function to retrieve the stored value
    function retrieve() public view returns (uint256) {
        return storedValue;
    }
}
```

---

### Ethereum Virtual Machine (EVM)
The EVM is a runtime environment for executing smart contracts and DApps on the Ethereum blockchain. It abstracts the underlying complexity of the network, allowing developers to write code in various programming languages that can be compiled into EVM bytecode. The EVM operates in a deterministic manner, ensuring that all nodes reach consensus on the state of the blockchain after executing transactions.

**Example: Deploying Smart Contract using Ethers.js**

```javascript
const { ethers } = require("ethers");

async function deployContract() {
    const provider = new ethers.providers.JsonRpcProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID");
    const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

    const abi = [ /* ABI from the compiled contract */ ];
    const bytecode = "0x..."; // Compiled contract bytecode

    const contractFactory = new ethers.ContractFactory(abi, bytecode, wallet);
    const contract = await contractFactory.deploy();
    console.log("Contract deployed at:", contract.address);
}

deployContract();
```

---

### Consensus Mechanism
Ethereum transitioned from Proof-of-Work (PoW) to Proof-of-Stake (PoS) consensus with the "Merge" on September 15, 2022. In PoS, validators are chosen to create new blocks based on the amount of ETH they hold and are willing to "stake" as collateral.

**Example: Setting up an Ethereum Validator for PoS (CLI)**

```bash
# Install eth2deposit-cli
pip install eth2deposit-cli

# Generate new Ethereum 2.0 keys
eth2deposit-cli new-mnemonic --num_validators 1 --chain mainnet

# Create the deposit
eth2deposit-cli generate-deposit --validator_keys /path/to/validator_keys --chain mainnet
```

---

### Gas Fees
Transactions on the Ethereum network require gas fees, paid in ETH. Gas serves as a measure of computational effort required to execute operations like transactions and smart contract executions.

**Example: Sending a Transaction with Gas Fees using Web3.js**

```javascript
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const tx = {
    from: '0xYourAddress',
    to: '0xRecipientAddress',
    value: web3.utils.toWei('0.1', 'ether'), 
    gas: 21000, 
    gasPrice: web3.utils.toWei('100', 'gwei') 
};

web3.eth.accounts.signTransaction(tx, 'YOUR_PRIVATE_KEY')
    .then(signedTx => web3.eth.sendSignedTransaction(signedTx.rawTransaction))
    .then(receipt => console.log('Transaction successful:', receipt.transactionHash))
    .catch(err => console.error('Error sending transaction:', err));
```
### Use Cases
Ethereum supports various applications across multiple domains:
- **Decentralized Finance (DeFi)**: Platforms built on Ethereum allow users to lend, borrow, trade, and earn interest without traditional financial intermediaries.
- **Non-Fungible Tokens (NFTs)**: Ethereum provides a framework for creating unique digital assets that represent ownership of specific items or content.
- **Decentralized Autonomous Organizations (DAOs)**: These entities operate through smart contracts, allowing members to govern collectively without centralized control.

# Visualising the results
![output_1](https://github.com/user-attachments/assets/61a5e7c6-5240-4ad2-959d-2aa712490aa5)
![output_2](https://github.com/user-attachments/assets/d06e7cab-9fe7-4961-8314-08b07bfb9207)
![output](https://github.com/user-attachments/assets/6e18ff07-a8a2-4486-872e-1a8af86f3d21)

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
