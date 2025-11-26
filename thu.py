import json
from web3 import Web3

# -------------------------
# 1. Cấu hình
# -------------------------
RPC_URL = "http://127.0.0.1:7545"  # Ganache URL
CONTRACT_ADDRESS = "0x765394046CC7de9FB46015b5FbeeD6F8f794d7FB"  # Update địa chỉ contract
PRIVATE_KEY = "0x65366c934773a5c180dd0059dea7d7ff7c02710ccf91242d1c01c6598b59cdab"

# ABI của contract (copy từ Remix)
CONTRACT_ABI = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_key",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_value",
				"type": "string"
			}
		],
		"name": "addAttribute",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			}
		],
		"name": "createIdentity",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "key",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "value",
				"type": "string"
			}
		],
		"name": "AttributeAdded",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "bytes32",
				"name": "credentialId",
				"type": "bytes32"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "issuer",
				"type": "address"
			}
		],
		"name": "CredentialIssued",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "bytes32",
				"name": "credentialId",
				"type": "bytes32"
			}
		],
		"name": "CredentialRevoked",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"name": "IdentityCreated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "bytes32",
				"name": "_credentialId",
				"type": "bytes32"
			}
		],
		"name": "issueCredential",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "bytes32",
				"name": "_credentialId",
				"type": "bytes32"
			}
		],
		"name": "revokeCredential",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_key",
				"type": "string"
			}
		],
		"name": "getAttribute",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getAttributeKeys",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getCredentialIds",
		"outputs": [
			{
				"internalType": "bytes32[]",
				"name": "",
				"type": "bytes32[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getName",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "nextId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "bytes32",
				"name": "_credentialId",
				"type": "bytes32"
			}
		],
		"name": "verifyCredential",
		"outputs": [
			{
				"internalType": "address",
				"name": "issuer",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "issuedAt",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "revoked",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
# -------------------------
# 2. Kết nối Web3
# -------------------------
w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("✗ Failed to connect to Ethereum network")
    exit(1)
print("✓ Connected to Ethereum network")

# Contract instance
contract_address = w3.to_checksum_address(CONTRACT_ADDRESS)
contract = w3.eth.contract(address=contract_address, abi=CONTRACT_ABI)
user_address = w3.eth.accounts[0]

# -------------------------
# 3. Tạo Transaction helper
# -------------------------
def send_transaction(tx):
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# -------------------------
# 4. Tạo Identity
# -------------------------
def create_identity(name):
    tx = contract.functions.createIdentity(name).build_transaction({
        'from': user_address,
        'nonce': w3.eth.get_transaction_count(user_address),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })
    send_transaction(tx)
    identity_id = contract.functions.nextId().call() - 1
    print(f"🎉 Identity created! ID = {identity_id}, Name = {name}")
    return identity_id

# -------------------------
# 5. Thêm Attribute
# -------------------------
def add_attribute(identity_id, key, value):
    tx = contract.functions.addAttribute(identity_id, key, value).build_transaction({
        'from': user_address,
        'nonce': w3.eth.get_transaction_count(user_address),
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    send_transaction(tx)
    print(f"✔ Added attribute ({key}: {value}) for identity ID {identity_id}")

# -------------------------
# 6. Issue & Revoke Credential
# -------------------------
def issue_credential(identity_id, credential_text):
    credential_id = w3.keccak(text=credential_text)
    tx = contract.functions.issueCredential(identity_id, credential_id).build_transaction({
        'from': user_address,
        'nonce': w3.eth.get_transaction_count(user_address),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })
    send_transaction(tx)
    print(f"🎓 Credential issued: {credential_id.hex()}")
    return credential_id

def revoke_credential(identity_id, credential_id):
    tx = contract.functions.revokeCredential(identity_id, credential_id).build_transaction({
        'from': user_address,
        'nonce': w3.eth.get_transaction_count(user_address),
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    send_transaction(tx)
    print(f"⚠ Credential revoked: {credential_id.hex()}")

# -------------------------
# 7. Đọc Attributes
# -------------------------
def read_attributes(identity_id):
    keys = contract.functions.getAttributeKeys(identity_id).call()
    attrs = {}
    for k in keys:
        v = contract.functions.getAttribute(identity_id, k).call()
        attrs[k] = v
    return attrs

# -------------------------
# 8. Lấy Event (web3.py >=6.x)
# -------------------------
# def get_contract_events(event_name, from_block=0, to_block="latest"):
#     try:
#         event_obj = getattr(contract.events, event_name)
#         logs = w3.eth.get_logs({
#             "fromBlock": from_block,
#             "toBlock": to_block,
#             "address": contract_address
#         })
#         decoded = [event_obj().process_log(log) for log in logs]
#         print(f"\n📌 Event List: {event_name}")
#         for evt in decoded:
#             print(f"- Block: {evt['blockNumber']}, Data: {evt['args']}")
#         return decoded
#     except Exception as e:
#         print(f"❌ Error fetching event {event_name}: {e}")
#         return None
def get_all_events():
    print("=== Reading all events ===")
    for event_abi in contract.events._events:
        event_name = event_abi['name']
        try:
            event = getattr(contract.events, event_name)
            # Tạo filter từ block 0 đến latest
            event_filter = event.create_filter(from_block=0)
            logs = event_filter.get_all_entries()
            for log in logs:
                print(f"\nEvent: {event_name}")
                print(log['args'])
        except Exception as e:
            print(f"Error reading {event_name}: {e}")
# -------------------------
# 9. Example Usage
# -------------------------
if __name__ == "__main__":
    # 1. Tạo Identity
    identity_id = create_identity("Alice")

    # 2. Thêm Attribute
    add_attribute(identity_id, "email", "alice@example.com")
    add_attribute(identity_id, "age", "20")

    # 3. Đọc Attribute
    attrs = read_attributes(identity_id)
    print("\nAttributes of identity:", attrs)

    # 4. Issue Credential
    cred_id = issue_credential(identity_id, "Degree_2025")

    # 5. Revoke Credential
    # revoke_credential(identity_id, cred_id)

    # 6. Lấy Event IdentityCreated và AttributeAdded
    get_all_events()
    
