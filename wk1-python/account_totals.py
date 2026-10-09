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
]

totals = {}

for txn in transactions:    
    account_type = account_types[txn["account"]]  
    print(f"{account_type}")  
    totals[account_type] = totals.get(account_type,0) + txn["amount"] 

for account_type, total in totals.items():
    print(f"{account_type}: ${total:,.2f}")