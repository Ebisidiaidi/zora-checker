from web3 import Web3
from tqdm import tqdm
import time

# Connect to Base network
w3 = Web3(Web3.HTTPProvider("https://base.publicnode.com"))

# Zora Rewards contract address (checksummed)
contract_address = w3.to_checksum_address("0x0000000002ba96c69b95e32caab8fc38bab8b3f8")

# ABI for accountClaim function
abi = [
    {
        "constant": True,
        "inputs": [{"name": "user", "type": "address"}],
        "name": "accountClaim",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]

# Load contract
contract = w3.eth.contract(address=contract_address, abi=abi)

# Read addresses from file
with open("address.txt", "r") as f:
    addresses = [line.strip() for line in f if line.strip()]

# Store results and error count
results = []
errors = 0

# Optional: Retry logic (uncomment to use)
# def safe_call(func, retries=3, delay=1):
#     for _ in range(retries):
#         try:
#             return func()
#         except Exception:
#             time.sleep(delay)
#     raise Exception("Max retries exceeded.")

# Check claims
for addr in tqdm(addresses, desc="Checking claims", unit="addr"):
    try:
        checksum_addr = w3.to_checksum_address(addr)
        claim_raw = contract.functions.accountClaim(checksum_addr).call()
        # claim_raw = safe_call(lambda: contract.functions.accountClaim(checksum_addr).call())
        claim_eth = w3.from_wei(claim_raw, 'ether')
        results.append((checksum_addr, claim_eth))
    except Exception as e:
        errors += 1
        print(f"\n⚠️ Error checking {addr}: {e}")

# Sort results by claim amount (descending)
results.sort(key=lambda x: x[1], reverse=True)

# Write to result.txt
with open("result.txt", "w") as f:
    for addr, amount in results:
        f.write(f"{addr} : {amount:,.4f} ZORA\n")

# Final summary
total_claimed = sum(amount for _, amount in results)
max_claim = max(results, key=lambda x: x[1], default=(None, 0))

print("\n📊 Summary")
print(f"✅ Total addresses checked: {len(addresses)}")
print(f"🟢 Successful queries: {len(results)}")
print(f"🔴 Failed queries: {errors}")
print(f"💰 Total ZORA claimed: {total_claimed:,.4f} ZORA")
if max_claim[0]:
    print(f"🏆 Highest single claim: {max_claim[1]:,.4f} ZORA ({max_claim[0]})")

print("\n✅ Done! Results written to result.txt")
