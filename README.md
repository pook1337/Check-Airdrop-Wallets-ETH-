
# Check-Airdrop-Wallets-ETH-

A Python tool to bulk check Ethereum wallet addresses for airdrop eligibility or balance status.

## Overview

**Check-Airdrop-Wallets-ETH-** is a Python-based CLI tool designed to help users verify multiple Ethereum wallet addresses in bulk. It can be used to check ETH balances, transaction counts, or other criteria relevant to airdrop eligibility.

This tool is ideal for developers, researchers, or crypto enthusiasts who want to automate the process of verifying wallets against airdrop requirements.

## Features

- Bulk processing of Ethereum wallet addresses from a file  
- Check ETH balance and transaction count for each wallet  
- Simple command-line interface for ease of use  
- Output results to CSV for further analysis  
- Uses `web3.py` for blockchain interaction  
- MIT licensed and open source

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pook1337/Check-Airdrop-Wallets-ETH-.git
   cd Check-Airdrop-Wallets-ETH-
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   *(If `requirements.txt` is not present, install manually:)*

   ```bash
   pip install web3 pandas
   ```

## Usage

Prepare a CSV or Excel file containing Ethereum wallet addresses with a column named `address`.

Run the script with your Ethereum node RPC URL (e.g., Infura or Alchemy):

```bash
python eth.py --input_file addresses.csv --output_file results.csv --rpc_url https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
```

### Arguments

- `--input_file`: Path to the input CSV or Excel file containing wallet addresses  
- `--output_file`: Path to save the output CSV file with balance and transaction data  
- `--rpc_url`: Ethereum node RPC URL for blockchain queries

## Example

```bash
python eth.py --input_file mywallets.csv --output_file checked_wallets.csv --rpc_url https://mainnet.infura.io/v3/abcdef1234567890
```

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open issues or submit pull requests.

