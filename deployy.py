from web3 import Web3
import json

# -----------------------------
# 1. Connect to Ganache
# -----------------------------
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    print("❌ Cannot connect to Ganache!")
    quit()

print("✔ Connected to Ganache")

# -----------------------------
# 2. Load ABI and Bytecode
# -----------------------------
with open("IdentityABI.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

with open("IdentityBytecode.txt", "r") as bytecode_file:
    contract_bytecode = bytecode_file.read().strip()

# -----------------------------
# 3. Set default account
# -----------------------------
web3.eth.default_account = web3.eth.accounts[0]

# -----------------------------
# 4. Deploy Contract
# -----------------------------
IdentityContract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

tx_hash = IdentityContract.constructor().transact()

print("⏳ Deploying contract...")

tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress

print("=====================================")
print("🎉 Contract deployed successfully!")
print("📌 Contract Address:", contract_address)
print("=====================================")

# Save address to file
with open("contract_address.txt", "w") as f:
    f.write(contract_address)
