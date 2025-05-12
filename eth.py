import argparse
import pandas as pd
from web3 import Web3

def load_addresses(file_path):
    # Supports CSV or Excel with a column 'address'
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    return df['address'].dropna().unique().tolist()

def check_wallet(w3, address):
    try:
        balance_wei = w3.eth.get_balance(address)
        balance_eth = w3.fromWei(balance_wei, 'ether')
        tx_count = w3.eth.get_transaction_count(address)
        return balance_eth, tx_count
    except Exception as e:
        print(f"Error checking {address}: {e}")
        return None, None

def main():
    parser = argparse.ArgumentParser(description='Bulk ETH Wallet Airdrop Checker')
    parser.add_argument('input_file', help='CSV or Excel file with Ethereum addresses (column name: address)')
    parser.add_argument('output_file', help='Output CSV file to save results')
    parser.add_argument('--rpc', required=True, help='Ethereum node RPC URL (Infura, Alchemy, etc.)')
    args = parser.parse_args()

    w3 = Web3(Web3.HTTPProvider(args.rpc))
    if not w3.isConnected():
        print("Failed to connect to Ethereum node. Check your RPC URL.")
        return

    addresses = load_addresses(args.input_file)
    print(f"Loaded {len(addresses)} addresses.")

    results = []
    for addr in addresses:
        balance, tx_count = check_wallet(w3, addr)
        if balance is not None:
            print(f"Address: {addr} | Balance: {balance} ETH | Tx Count: {tx_count}")
            results.append({'address': addr, 'balance_eth': balance, 'tx_count': tx_count})

    df_out = pd.DataFrame(results)
    df_out.to_csv(args.output_file, index=False)
    print(f"Results saved to {args.output_file}")

if __name__ == '__main__':
    main()
