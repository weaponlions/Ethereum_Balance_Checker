# transfer_assets.py

import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
INFURA_URL = f'https://mainnet.infura.io/v3/52e33221614d4a48a6881c7138b1aea5'
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Initialize Web3   
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# ERC-20 Token ABI to interact with
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "to", "type": "address"}, {"name": "value", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

def transfer_eth(from_address, to_address, amount):
    nonce = web3.eth.getTransactionCount(from_address)
    gas_price = web3.eth.gas_price
    transaction = {
        'to': to_address,
        'value': web3.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': gas_price,
        'nonce': nonce,
    }

    signed_transaction = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash

def transfer_erc20(from_address, to_address, amount, token_address):
    contract = web3.eth.contract(address=token_address, abi=ERC20_ABI)
    nonce = web3.eth.getTransactionCount(from_address)
    gas_price = web3.eth.gas_price

    transaction = contract.functions.transfer(to_address, web3.toWei(amount, 'ether')).buildTransaction({
        'chainId': 1,
        'gas': 200000,
        'gasPrice': gas_price,
        'nonce': nonce,
    })

    signed_transaction = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash

def move_assets(addresses, target_address, tokens):
    for address in addresses:
        eth_balance = web3.eth.get_balance(address)
        if eth_balance > 0:
            print(f"Transferring {web3.fromWei(eth_balance, 'ether')} ETH from {address} to {target_address}")
            tx_hash = transfer_eth(address, target_address, web3.fromWei(eth_balance, 'ether'))
            print(f"ETH transfer tx hash: {tx_hash.hex()}")

        for token in tokens:
            token_balance = get_erc20_balance(address, token['address'])
            if token_balance > 0:
                print(f"Transferring {token_balance} {token['symbol']} from {address} to {target_address}")
                tx_hash = transfer_erc20(address, target_address, token_balance, token['address'])
                print(f"ERC-20 transfer tx hash: {tx_hash.hex()}")
