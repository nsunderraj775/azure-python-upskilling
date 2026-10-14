deposits = [

{"branch": "ATL", "customer": "C01","amount": 1500.00},
{"branch": "PHL", "customer": "C02","amount": 2600.00},
{"branch": "ATL", "customer": "C03","amount": 4200.00},
{"branch": "NYC", "customer": "C01","amount": 800.00},
{"branch": "PHL", "customer": "C04","amount": 3100.00},
{"branch": "NYC", "customer": "C05","amount": 95.00},
]
branchtotals = {}
for dep in deposits:
     branch = dep["branch"]
     branchtotals[branch] = branchtotals.get(branch,0) + dep["amount"]
for deposit,totals in branchtotals.items():
    print(f"{deposit}: ${totals:,.2f}")
customers= set()
for dep in deposits:
     customers.add(dep["customer"])
print(f"Customers:{customers}")
print(f"Number of customers: {len(customers)}")
bigcustomers = [dep['customer'] for dep in deposits if dep['amount'] > 1000 ]
print(f"Customer having more than 1000: {bigcustomers}")
top_branch =  ""
top_branch1 = ""
top_amount = 0

for branch,amount in branchtotals.items():
     if amount > top_amount:
        top_amount = amount
        top_branch = branch         
print(f"Top branch: {top_branch} with ${top_amount:,.2f}")
highamount = []
top_amount = max(branchtotals.values())
top_branches = [branch for branch, amount in branchtotals.items() if amount == top_amount]
print(f"Top branches: {top_branches} with ${top_amount:,.2f}")