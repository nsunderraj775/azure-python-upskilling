chart_of_accounts = {
    "1000": "Cash",
    "1200": "Accounts Receivable",
    "2000": "Accounts Payable",
    "4000": "Revenue",
    "5000": "Operating Expense",
}

print(chart_of_accounts["4000"])
chart_of_accounts["6000"] = "Interest Expense"
chart_of_accounts["0700"] = "Loans"
for code,name  in chart_of_accounts.items():
    print(f"{code}: {name}")
transactions = [
    {"id": 1, "account": "1000", "amount": 5000.00},
    {"id": 2, "account": "4000", "amount": 1200.00},
    {"id": 3, "account": "5000", "amount": 350.75},
]

for txn in transactions:
    print(f"Txn {txn['id']}: account {txn['account']}, ${txn['amount']:,.2f}")
