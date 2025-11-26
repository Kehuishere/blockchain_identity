from web3 import Web3

# -------------------------
# 1. Cấu hình kết nối Ganache
# -------------------------
RPC_URL = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(RPC_URL))
assert w3.is_connected, "❌ Không kết nối được với Ganache"

accounts = w3.eth.accounts
deployer = accounts[0]

# -------------------------
# 2. ABI & Contract Address
# -------------------------
CONTRACT_ADDRESS = "0xe6E2519be551303ea790ed4F40f5e7Cc01ef6ac2"  # update địa chỉ contract
with open("IdentityABI.json", "r") as f:
    abi = f.read()

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

# -------------------------
# 3. Tạo Identity
# -------------------------
print("📌 Tạo identity Alice")
tx_create = contract.functions.createIdentity("Alice").transact({"from": deployer})
w3.eth.wait_for_transaction_receipt(tx_create)

# Lấy id vừa tạo (giả sử contract có nextIdentityId)
# Lấy giá trị nextId từ contract
identity_id = contract.functions.nextId().call() - 1
print("Last identity id:", identity_id)


# -------------------------
# 4. Thêm Attribute
# -------------------------
print("📌 Thêm attribute email")
tx_attr = contract.functions.addAttribute(identity_id, "email", "alice@example.com").transact({"from": deployer})
w3.eth.wait_for_transaction_receipt(tx_attr)
print("✅ Attribute added")

# -------------------------
# 5. Issue Credential
# -------------------------
print("📌 Issue credential 'degree'")
from web3 import Web3

# Chuyển string thành bytes32
raw_bytes = b"degree"
credential_id = raw_bytes.ljust(32, b'\0')  # padding thêm 0 đến đủ 32 bytes

# Bây giờ gọi hàm contract
tx_cred = contract.functions.issueCredential(identity_id, credential_id).transact({"from": deployer})

print("✅ Credential issued")

# -------------------------
# 6. Revoke Credential
# -------------------------
print("📌 Revoke credential 'degree'")
tx_revoke = contract.functions.revokeCredential(identity_id, credential_id).transact({"from": deployer})
w3.eth.wait_for_transaction_receipt(tx_revoke)
print("✅ Credential revoked")

# -------------------------
# 7. Lấy Identity info
# -------------------------
identity_info = contract.functions.getIdentityInfo(identity_id).call()
print("📋 Identity info:", identity_info)
