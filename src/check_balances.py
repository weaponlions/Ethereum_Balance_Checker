from web3 import Web3
import requests
from decimal import Decimal

Metamask_Key = "52e33221614d4a48a6881c7138b1aea5"


INFURA_URL = f'https://mainnet.infura.io/v3/{Metamask_Key}'

# Initialize Web3 with Infura
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# CoinGecko API URL for token price and volume
COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/'

# ERC-20 Token ABI (simplified)
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Function to get Ethereum balance
def get_eth_balance(address):
    balance_wei = web3.eth.get_balance(address)
    return web3.from_wei(balance_wei, 'ether')  # Convert from Wei to Ether

# Function to get ERC-20 token balance
def get_erc20_balance(address, token_address):
    contract = web3.eth.contract(address=token_address, abi=ERC20_ABI)
    balance = contract.functions.balanceOf(address).call()
    return web3.fromWei(balance, 'ether')  # Convert from Wei to token units

# Function to fetch token price and volume using CoinGecko
def get_token_data(token_id):
    url = f'{COINGECKO_API_URL}coins/{token_id}'
    response = requests.get(url)
    data = response.json()
    price = data['market_data']['current_price']['usd']
    volume = data['market_data']['total_volume']['usd']
    return price, volume


token_ids = [
    "ethereum",        # Ethereum (ETH)
    "tether",          # Tether (USDT)
    "usd-coin",        # USD Coin (USDC)
    "binancecoin",     # Binance Coin (BNB)
    "dogecoin",        # Dogecoin (DOGE)
    "chainlink",       # Chainlink (LINK)
    "uniswap",         # Uniswap (UNI)
    "matic-network",   # Polygon (MATIC)
    "cardano",         # Cardano (ADA)
    "litecoin",        # Litecoin (LTC)
    "shiba-inu",       # Shiba Inu (SHIB)
    "wrapped-bitcoin", # Wrapped Bitcoin (WBTC)
    "dai",             # Dai (DAI)
    "avalanche-2",     # Avalanche (AVAX)
    "solana",          # Solana (SOL)
    "aave",            # Aave (AAVE)
    "sushiswap",       # SushiSwap (SUSHI)
    "terra-luna",      # Terra (LUNA)
    "fantom",          # Fantom (FTM)
    "pancakeswap-token", # PancakeSwap (CAKE)
    "uniswap",         # Uniswap (UNI)
    "binancecoin",     # Binance Coin (BNB)
    "cosmos",          # Cosmos (ATOM)
    "filecoin",        # Filecoin (FIL)
    "vechain",         # VeChain (VET)
    "polkadot",        # Polkadot (DOT)
    "litecoin",        # Litecoin (LTC)
    "monero",          # Monero (XMR)
    "xrp",             # XRP (XRP)
    "tezos",           # Tezos (XTZ)
    "tron",            # TRON (TRX)
]



eth_address = '0xf16437f60e84E22d4C2bD86BbD9523D5e7502B52'
eth_balance = get_eth_balance(eth_address)
token_price, token_volume = get_token_data(token_ids[0])

eth_balance = Decimal(eth_balance)  
token_price = Decimal(token_price) 
eth_balance_in_usdt = eth_balance * token_price

print(f"Ethereum Balance: {eth_balance} ETH")
print(f"Ethereum Balance In Usdt: ${eth_balance_in_usdt}")
print(f"Token Price: ${token_price}")
print(f"24h Trading Volume: ${token_volume}")


