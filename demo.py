from web3 import Web3
import json

RPC_URL = "http://127.0.0.1:7545"

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Check connection
if w3.is_connected():
    print("✓ Connected to Ethereum network")
    print(f"Latest block: {w3.eth.block_number}")
else:
    print("✗ Failed to connect to Ethereum network")
    exit(1)

# Contract address
CONTRACT_ADDRESS = "0xA7be44EbE223D8977b1667B777B927283BC6e4A5"

# Contract ABI 
CONTRACT_ABI = [
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "num",
                "type": "uint256"
            }
        ],
        "name": "store",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "retrieve",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Convert address to checksum format
contract_address = w3.to_checksum_address(CONTRACT_ADDRESS)

# Create contract instance
contract = w3.eth.contract(address=contract_address, abi=CONTRACT_ABI)

print(f"\nContract Address: {contract_address}")

# Example 1: Call a read-only function (no gas required)
def read_contract_data():
    """Call a view/pure function that doesn't modify state"""
    try:
        # Calling retrieve() function
        result = contract.functions.retrieve().call()
        print(f"\n📖 Read Operation:")
        print(f"Current stored number: {result}")
        return result
    except Exception as e:
        print(f"Error reading contract: {e}")
        return None

# Example 2: Send a transaction (requires gas and private key)
def write_contract_data(new_value, private_key, from_address):
    """Send a transaction that modifies contract state"""
    try:
        # Get nonce
        nonce = w3.eth.get_transaction_count(from_address)
        
        # Build transaction
        transaction = contract.functions.store(new_value).build_transaction({
            'from': from_address,
            'nonce': nonce,
            'gas': 200000,
            'gasPrice': w3.eth.gas_price,
            'chainId': w3.eth.chain_id
        })
        
        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        
        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"\n📝 Write Operation:")
        print(f"Transaction hash: {tx_hash.hex()}")
        
        # Wait for transaction receipt
        print("Waiting for transaction confirmation...")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction confirmed in block: {tx_receipt['blockNumber']}")
        print(f"Gas used: {tx_receipt['gasUsed']}")
        
        return tx_receipt
    except Exception as e:
        print(f"Error writing to contract: {e}")
        return None

# Example 3: Get contract events/logs
def get_contract_events(event_name, from_block=0, to_block='latest'):
    """Retrieve past events from the contract"""
    try:
        event_filter = getattr(contract.events, event_name).create_filter(
            fromBlock=from_block,
            toBlock=to_block
        )
        events = event_filter.get_all_entries()
        print(f"\n📋 Events ({event_name}):")
        for event in events:
            print(f"Block: {event['blockNumber']}, Data: {event['args']}")
        return events
    except Exception as e:
        print(f"Error getting events: {e}")
        return None

# Example 4: Check account balance
def check_balance(address):
    """Check ETH balance of an address"""
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    print(f"\n💰 Balance of {address}:")
    print(f"{balance_eth} ETH")
    return balance_eth

# Example 5: Estimate gas for a transaction
def estimate_gas(function_call, from_address):
    """Estimate gas needed for a transaction"""
    try:
        gas_estimate = function_call.estimate_gas({'from': from_address})
        print(f"\n⛽ Estimated gas: {gas_estimate}")
        return gas_estimate
    except Exception as e:
        print(f"Error estimating gas: {e}")
        return None

# Main execution
if __name__ == "__main__":
    print("\n" + "="*50)
    print("WEB3 SMART CONTRACT INTERACTION")
    print("="*50)
    
    # Read current stored value
    current_value = read_contract_data()
    
    # Display detailed information
    print("\n" + "="*50)
    print("DETAILED INFORMATION")
    print("="*50)
    
    # Network Information
    print("\n🌐 Network Information:")
    print(f"   Connected to: {RPC_URL}")
    print(f"   Chain ID: {w3.eth.chain_id}")
    print(f"   Latest Block Number: {w3.eth.block_number}")
    print(f"   Gas Price: {w3.from_wei(w3.eth.gas_price, 'gwei')} Gwei")
    
    # Contract Information
    print("\n📝 Contract Information:")
    print(f"   Address: {contract_address}")
    print(f"   Current Stored Value: {current_value}")
    print(f"   Available Functions:")
    print(f"      - retrieve() : Read stored number (view)")
    print(f"      - store(uint256) : Store new number (payable)")
    
    # Get bytecode to verify contract exists
    bytecode = w3.eth.get_code(contract_address)
    print(f"   Contract Deployed: {'Yes' if len(bytecode) > 2 else 'No'}")
    print(f"   Bytecode Size: {len(bytecode)} bytes")
    
    # Account Information (if available)
    print("\n👤 Available Accounts:")
    try:
        accounts = w3.eth.accounts
        if accounts:
            for idx, account in enumerate(accounts[:3]):  # Show first 3 accounts
                balance = w3.eth.get_balance(account)
                balance_eth = w3.from_wei(balance, 'ether')
                print(f"   [{idx}] {account}")
                print(f"       Balance: {balance_eth} ETH")
        else:
            print("   No accounts available (use private key for transactions)")
    except Exception as e:
        print(f"   Could not retrieve accounts: {e}")
    
   
 
    # Estimate gas for storing a value
    print("\n⛽ Gas Estimation:")
    try:
        if accounts:
            gas_estimate = contract.functions.store(100).estimate_gas({'from': accounts[0]})
            print(f"   Estimated gas for store(100): {gas_estimate} gas units")
            gas_cost_wei = gas_estimate * w3.eth.gas_price
            gas_cost_eth = w3.from_wei(gas_cost_wei, 'ether')
            print(f"   Estimated cost: {gas_cost_eth} ETH (~{w3.from_wei(gas_cost_wei, 'gwei')} Gwei)")
    except Exception as e:
        print(f"   Gas estimation unavailable: {e}")
    
    print("\n" + "="*50)
    print("✓ Script completed successfully!")
    print("="*50)


