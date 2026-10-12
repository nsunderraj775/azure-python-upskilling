account_types = {
    "1000":"Asset",
    "1200":"Asset",
    "2000":"Liability",
    "4000":"Revenue",
    "5000":"Expense",
    "6000":"Expense",
}

transactions = [
    {"id": 1, "account": "1000", "amount": 5000.00},
    {"id": 2, "account": "4000", "amount": 1200.00},
    {"id": 3, "account": "5000", "amount": 350.75},
    {"id": 4, "account": "1200", "amount": 2400.00},
    {"id": 5, "account": "6000", "amount": 89.50},
    {"id": 6, "account": "4000", "amount": 3100.00},
    {"id": 7, "account": "5000", "amount": 720.25},
    {"id": 8, "account": "2000", "amount": 1500.00},    
    {"id": 9, "account": "9999", "amount": 500.00},
    {"id": 10, "account": "8888", "amount": 75.00},
]
valid_transactions = []
rejected = []
for txn in transactions:
    if txn["account"] in account_types:
        valid_transactions.append(txn)
    else:       
        print(f"DQ warning: transaction {txn['id']} has unknown account {txn['account']} - skipped")
        rejected.append(txn["id"])
print(f"Rejected: {rejected}")
print(f"Reconciliation: {len(valid_transactions)} valid + {len(rejected)} rejected  = {len(transactions)} total")
amounts = []
large_count = 0 
large_total = 0
for txn in valid_transactions:    
    amounts.append(txn["amount"]) 
total = sum(amounts)
count = len(amounts)
Average = (total / count)    
print(f"Count: {len(amounts)}")
print(f"Sum: ${sum(amounts):,.2f}")
print(f"Max: ${max(amounts):,.2f}")
print(f"Min: ${min(amounts):,.2f}")
print(f"Average: ${(Average):,.2f}")
for txn in valid_transactions:
    if txn["amount"] > 1000:
            large_count = large_count + 1
            large_total = large_total + txn["amount"]
print(f"Large Count: {large_count}")
print(f"Large Total: ${large_total:,.2f}")
counts = {}
for txn in valid_transactions:
     account_type = account_types[txn["account"]]
     counts[account_type] = counts.get(account_type,0) + 1

for account_type, num in counts.items():
    print(f"{account_type}: {num}")