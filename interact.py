# import json
# from web3 import Web3

# # -------------------------
# # 1. Cấu hình
# # -------------------------
# RPC_URL = "http://127.0.0.1:7545"
# CONTRACT_ADDRESS = "0xBD7C7cb6bB06992abAD866f8bf3E821F0F67e0D3"

# w3 = Web3(Web3.HTTPProvider(RPC_URL))
# if not w3.is_connected():
#     raise ConnectionError("✗ Failed to connect to Ethereum network")
# print("✓ Connected to Ethereum network")

# # Ganache accounts
# owner = w3.eth.accounts[0]
# issuer = w3.eth.accounts[1]
# verifier = w3.eth.accounts[2]

# PRIVATE_KEYS = {
#     owner: "0xca537952516f2a7f99b09ab000af8964349189b10c25df4c633fc7e2867d44cb",
#     issuer: "0x3e25365e164832e51a0d99708c081ce525b29a272c360d726c036944f7f65172",
#     verifier: "0xd72121a69374d4338541e20384b4aad1edb38dedee25c8f29b862a9772deaa18"
# }

# # ABI (giữ nguyên ABI từ Remix)
# # CONTRACT_ABI = [
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_key",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_value",
# 				"type": "string"
# 			}
# 		],
# 		"name": "addAttribute",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "uint256",
# 				"name": "id",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "string",
# 				"name": "key",
# 				"type": "string"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "string",
# 				"name": "value",
# 				"type": "string"
# 			}
# 		],
# 		"name": "AttributeAdded",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "_issuer",
# 				"type": "address"
# 			}
# 		],
# 		"name": "authorizeIssuer",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "string",
# 				"name": "_name",
# 				"type": "string"
# 			}
# 		],
# 		"name": "createIdentity",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "uint256",
# 				"name": "id",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": True,
# 				"internalType": "bytes32",
# 				"name": "credentialId",
# 				"type": "bytes32"
# 			},
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "issuer",
# 				"type": "address"
# 			}
# 		],
# 		"name": "CredentialIssued",
# 		"type": "event"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "uint256",
# 				"name": "id",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": True,
# 				"internalType": "bytes32",
# 				"name": "credentialId",
# 				"type": "bytes32"
# 			}
# 		],
# 		"name": "CredentialRevoked",
# 		"type": "event"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "uint256",
# 				"name": "id",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "owner",
# 				"type": "address"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "string",
# 				"name": "name",
# 				"type": "string"
# 			}
# 		],
# 		"name": "IdentityCreated",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "bytes32",
# 				"name": "_credentialId",
# 				"type": "bytes32"
# 			}
# 		],
# 		"name": "issueCredential",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "uint256",
# 				"name": "id",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "issuer",
# 				"type": "address"
# 			}
# 		],
# 		"name": "IssuerAuthorized",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "bytes32",
# 				"name": "_credentialId",
# 				"type": "bytes32"
# 			}
# 		],
# 		"name": "revokeCredential",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "newOwner",
# 				"type": "address"
# 			}
# 		],
# 		"name": "transferOwnership",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_key",
# 				"type": "string"
# 			}
# 		],
# 		"name": "getAttribute",
# 		"outputs": [
# 			{
# 				"internalType": "string",
# 				"name": "",
# 				"type": "string"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getAttributeKeys",
# 		"outputs": [
# 			{
# 				"internalType": "string[]",
# 				"name": "keys",
# 				"type": "string[]"
# 			},
# 			{
# 				"internalType": "string[]",
# 				"name": "values",
# 				"type": "string[]"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getCredentialIds",
# 		"outputs": [
# 			{
# 				"internalType": "bytes32[]",
# 				"name": "",
# 				"type": "bytes32[]"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getIdentityInfo",
# 		"outputs": [
# 			{
# 				"internalType": "address",
# 				"name": "owner",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "name",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string[]",
# 				"name": "attributeKeys",
# 				"type": "string[]"
# 			},
# 			{
# 				"internalType": "string[]",
# 				"name": "attributeValues",
# 				"type": "string[]"
# 			},
# 			{
# 				"internalType": "bytes32[]",
# 				"name": "credentialIds",
# 				"type": "bytes32[]"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getName",
# 		"outputs": [
# 			{
# 				"internalType": "string",
# 				"name": "",
# 				"type": "string"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getOwner",
# 		"outputs": [
# 			{
# 				"internalType": "address",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "nextId",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_id",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "bytes32",
# 				"name": "_credentialId",
# 				"type": "bytes32"
# 			}
# 		],
# 		"name": "verifyCredential",
# 		"outputs": [
# 			{
# 				"internalType": "address",
# 				"name": "issuer",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "issuedAt",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "bool",
# 				"name": "revoked",
# 				"type": "bool"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	}
# ]# paste ABI của bạn vào đây
# with open("IdentityABI.json", "r") as abi_file:
#     contract_abi = json.load(abi_file)
# # Contract instance
# contract = w3.eth.contract(address=w3.to_checksum_address(CONTRACT_ADDRESS), abi=contract_abi)

# # -------------------------
# # 2. Transaction helper
# # -------------------------
# def send_transaction(tx, from_address):
#     signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEYS[from_address])
#     tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)  # lowercase
#     receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#     return receipt


# # -------------------------
# # 3. Identity
# # -------------------------
# def create_identity(name, owner_addr):
#     tx = contract.functions.createIdentity(name).build_transaction({
#         'from': owner_addr,
#         'nonce': w3.eth.get_transaction_count(owner_addr),
#         'gas': 300_000,
#         'gasPrice': w3.eth.gas_price
#     })
#     send_transaction(tx, owner_addr)
#     identity_id = contract.functions.nextId().call() - 1
#     print(f"🎉 Identity created: ID={identity_id}, Name={name}")
#     return identity_id

# def add_attribute(identity_id, key, value, owner_addr):
#     tx = contract.functions.addAttribute(identity_id, key, value).build_transaction({
#         'from': owner_addr,
#         'nonce': w3.eth.get_transaction_count(owner_addr),
#         'gas': 200_000,
#         'gasPrice': w3.eth.gas_price
#     })
#     send_transaction(tx, owner_addr)
#     print(f"✔ Attribute added: {key}={value} for identity {identity_id}")

# def read_attributes(identity_id):
#     try:
#         keys, _ = contract.functions.getAttributeKeys(identity_id).call()
#         attrs = {k: contract.functions.getAttribute(identity_id, k).call() for k in keys}
#         return attrs
#     except Exception as e:
#         print(f"❌ Error reading attributes: {e}")
#         return {}

# # -------------------------
# # 4. Credential
# # -------------------------
# def issue_credential(identity_id, credential_text, issuer_addr):
#     credential_id = w3.keccak(text=credential_text)
#     tx = contract.functions.issueCredential(identity_id, credential_id).build_transaction({
#         'from': issuer_addr,
#         'nonce': w3.eth.get_transaction_count(issuer_addr),
#         'gas': 300_000,
#         'gasPrice': w3.eth.gas_price
#     })
#     send_transaction(tx, issuer_addr)
#     print(f"🎓 Credential issued: {credential_id.hex()}")
#     return credential_id

# def revoke_credential(identity_id, credential_id, issuer_addr):
#     tx = contract.functions.revokeCredential(identity_id, credential_id).build_transaction({
#         'from': issuer_addr,
#         'nonce': w3.eth.get_transaction_count(issuer_addr),
#         'gas': 200_000,
#         'gasPrice': w3.eth.gas_price
#     })
#     send_transaction(tx, issuer_addr)
#     print(f"⚠ Credential revoked: {credential_id.hex()}")

# def verify_credential(identity_id, credential_id):
#     issuer_addr, issued_at, revoked = contract.functions.verifyCredential(identity_id, credential_id).call()
#     print(f"✔ Credential verification:\n  Issuer: {issuer_addr}\n  IssuedAt: {issued_at}\n  Revoked: {revoked}")
#     return issuer_addr, issued_at, revoked

# # -------------------------
# # 5. Event helper
# # -------------------------
# def get_all_events():
#     print("=== All Events ===")
#     for event_name in contract.events._events:
#         try:
#             event = getattr(contract.events, event_name['name'])
#             logs = event.create_filter(from_block=0, to_block='latest').get_all_entries()
#             for log in logs:
#                 print(f"\nEvent: {event_name['name']}")
#                 print(log['args'])
#         except Exception as e:
#             print(f"❌ Error reading {event_name['name']}: {e}")

# # -------------------------
# # 6. Example workflow
# # -------------------------
# if __name__ == "__main__":
#     # 1️⃣ Owner tạo identity & thêm attributes
#     identity_id = create_identity("Alice", owner)
#     add_attribute(identity_id, "email", "alice@example.com", owner)
#     add_attribute(identity_id, "age", "20", owner)

#     # 2️⃣ Owner authorize issuer
#     tx = contract.functions.authorizeIssuer(identity_id, issuer).build_transaction({
#         'from': owner,
#         'nonce': w3.eth.get_transaction_count(owner),
#         'gas': 200_000,
#         'gasPrice': w3.eth.gas_price
#     })
#     send_transaction(tx, owner)
#     print(f"✅ Issuer {issuer} authorized for identity {identity_id}")

#     # 3️⃣ Issuer cấp credential
#     cred_id = issue_credential(identity_id, "Degree_2025", issuer)

#     # 4️⃣ Verifier kiểm tra credential
#     verify_credential(identity_id, cred_id)

#     # 5️⃣ Đọc attributes
#     attrs = read_attributes(identity_id)
#     print("\nAttributes:", attrs)

#     # 6️⃣ Lấy tất cả event
#     get_all_events()

from web3 import Web3
import json

# =========================
# 1. Kết nối Ganache
# =========================
RPC_URL = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    print("✗ Failed to connect to Ethereum network")
    exit(1)

print("✓ Connected to Ethereum network")

# =========================
# 2. Load contract
# =========================
CONTRACT_ADDRESS = "0x836C353009e73c8654134D815aC29052108fbb39"

with open("IdentityABI.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

# =========================
# 3. Tài khoản Ganache
# =========================
holder   = w3.eth.accounts[4]
issuer   = w3.eth.accounts[0]
verifier = w3.eth.accounts[2]

print("\n=== Decentralized Identity Demo ===")
print(f"Holder:   {holder}")
print(f"Issuer:   {issuer}")
print(f"Verifier: {verifier}")

# =========================
# 4. Helper functions
# =========================
def create_identity(holder, name="Ngoc Le"):
    tx = contract.functions.createIdentity(name).transact({'from': holder})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt
def get_all_events():
    print("=== All Events ===")
    for event_name in contract.events._events:
        try:
            event = getattr(contract.events, event_name['name'])
            logs = event.create_filter(from_block=0, to_block='latest').get_all_entries()
            for log in logs:
                print(f"\nEvent: {event_name['name']}")
                print(log['args'])
        except Exception as e:
            print(f"❌ Error reading {event_name['name']}: {e}")
def add_attribute(holder, identity_id, key, value):
    tx = contract.functions.addAttribute(identity_id, key, value).transact({'from': holder})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt

def authorize_issuer(identity_id, holder_addr, issuer_addr):
    tx = contract.functions.authorizeIssuer(identity_id, issuer_addr).transact({'from': holder_addr})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt

def issue_credential(issuer_addr, identity_id, cred_text):
    cred_id = w3.keccak(text=cred_text)
    tx = contract.functions.issueCredential(identity_id, cred_id).transact({'from': issuer_addr})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt, cred_id
def check_balance(address):
    """Check ETH balance of an address"""
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    print(f"\n💰 Balance of {address}:")
    print(f"{balance_eth} ETH")
    return balance_eth


# =========================
# 5. DEMO WORKFLOW
# =========================
if __name__ == "__main__":

    # 1️⃣ Create Identity
    # input("=== 1. Holder tạo danh tính (nhấn ENTER) ===")
    # rc = create_identity(holder)

    # events = contract.events.IdentityCreated().process_receipt(rc)
    # for e in events:
    #     print("=== Event IdentityCreated ===")
    #     print(e['args'])

    # identity_id = events[0]['args']['id']
    input("=== 1. Holder tạo danh tính (nhấn ENTER) ===")
rc = create_identity(holder)

events = contract.events.IdentityCreated().process_receipt(rc)

if len(events) == 0:
    print("❌ Không tìm thấy event IdentityCreated trong transaction!")
    print("➡ Có thể function tạo danh tính không emit event, hoặc bị revert.")
    print("➡ Hãy kiểm tra lại contract và hàm create_identity().")
else:
    for e in events:
        print("=== Event IdentityCreated ===")
        print(e['args'])

    identity_id = events[0]['args']['id']
    print("➡ identity_id =", identity_id)

    # 2️⃣ Add attribute
    input("=== 2. Thêm Attribute Name (nhấn ENTER) ===")
    rc = add_attribute(holder, identity_id, "Name", "Ngoc Le")

    events = contract.events.AttributeAdded().process_receipt(rc)
    for e in events:
        print("=== Event AttributeAdded ===")
        print(e['args'])

    # 3️⃣ Authorize issuer
    input("=== 3. Owner authorize issuer (nhấn ENTER) ===")
    rc = authorize_issuer(identity_id, holder, issuer)

    events = contract.events.IssuerAuthorized().process_receipt(rc)
    for e in events:
        print("=== Event IssuerAuthorized ===")
        print(e['args'])

    # 4️⃣ Issue credential
    input("=== 4. Issuer cấp Credential (nhấn ENTER) ===")
    rc, cred_id = issue_credential(issuer, identity_id, "CRED001")

    events = contract.events.CredentialIssued().process_receipt(rc)
    for e in events:
        print("=== Event CredentialIssued ===")
        print(e['args'])
        
check_balance(w3.eth.accounts[4])
check_balance(w3.eth.accounts[0])
check_balance(w3.eth.accounts[2])
print(add_attribute(holder, identity_id, "Name", "Ngoc"))

