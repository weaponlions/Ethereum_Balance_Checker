# Ethereum Balance Checker

This Python project is designed to interact with Ethereum addresses and ERC-20 tokens. The current functionality allows checking balances of Ethereum and ERC-20 tokens. The next steps involve adding the ability to transfer assets once testnet Ethereum is available.

## Features

- **Check Ethereum Balance**: Fetch and display the Ethereum (ETH) balance for a given address.
- **Check ERC-20 Token Balance**: Fetch and display the balance of any ERC-20 token (e.g., USDT, UNI) for a given address.
- **Fetch Token Price & 24h Volume**: Retrieve the current price and 24-hour trading volume of a specific ERC-20 token from CoinGecko.

### Planned Features:
- **Transfer Ethereum**: Implement functionality to transfer Ethereum (ETH) from one address to another.
- **Transfer ERC-20 Tokens**: Implement functionality to transfer ERC-20 tokens between addresses.
- **Testnet Ethereum Solution**: Create a testnet environment using Ropsten or Rinkeby testnet to safely test the transfer functions before using mainnet.

## Requirements

- Python 3.7 or higher
- Libraries: `web3`, `requests`, `decimal`
- Infura API key for connecting to Ethereum network (Mainnet or Testnet)
- A CoinGecko API endpoint for fetching token price and volume data

## Installation

### 1. Clone the Repository
```bash
git clone repo_link
cd eth-balance-checker
```

### 2. Create a Virtual Environment & Install Required Dependencies
```bash
run setup.sh in bash terminal
```


## How to Use

### 1. **Check Ethereum Balance**
To check the balance of an Ethereum address, run the script `check_balances.py`. Replace `eth_address` with the desired Ethereum address.

```bash
python check_balances.py
```

### 2. **Check ERC-20 Token Balance**
Replace `eth_address` and `token_address` in the script with the desired Ethereum address and ERC-20 token contract address (e.g., USDT or UNI token). 

### 3. **Fetch Token Price & Volume**
To get the price and 24-hour trading volume of a specific token, use the `get_token_data()` function in your code with the appropriate CoinGecko token ID.

## Testnet Ethereum Solution (To Be Implemented)

For transferring Ethereum and ERC-20 tokens, we will first test the functionality on a **testnet** (such as Ropsten or Rinkeby) to ensure safety and prevent any potential loss of funds on the main Ethereum network.

### Steps to Set Up a Testnet Environment:

1. **Infura Testnet Endpoint**: You can get Ropsten or Rinkeby testnet endpoints from Infura. Replace the `INFURA_API_KEY` in the `.env` file with the relevant API key for the testnet.

2. **Testnet ETH**: Obtain testnet ETH (Ropsten or Rinkeby) from a faucet:
   - [Ropsten Faucet](https://faucet.ropsten.be/)
   - [Rinkeby Faucet](https://faucet.rinkeby.io/)

3. **Testing Transfers**: Once you have testnet ETH and your Ethereum address configured, you will be able to test transferring ETH and ERC-20 tokens between addresses.

**Note**: For the transfer functionality, you will need to use private keys (be careful with security). Never expose private keys in the code. Use environment variables or secure methods to manage them.

## Example of Future Transfers Implementation

The transfer functionality (to be implemented) will require the following steps:

- **Transfer ETH**: 
  - Use `web3.eth.sendTransaction()` method to send ETH from one address to another.
  - Sign the transaction with a private key (using `web3.eth.account`).
  
- **Transfer ERC-20 Tokens**:
  - Use the ERC-20 token contract's `transfer()` function (through `web3.eth.contract`).
  - Ensure the correct allowance and approval if needed.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Conclusion:

The project is currently focused on checking balances of Ethereum and ERC-20 tokens, with transfer functionality planned for later once testnet Ethereum solutions are set up. This README serves as a guide to getting started and understanding the current state of the project, with the goal of future enhancements.

Let me know if you need further details or modifications!
