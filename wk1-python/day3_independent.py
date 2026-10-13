deposits = [

{"branch": "ATL", "customer": "C01","amount": 1500.00},
{"branch": "PHL", "customer": "C02","amount": 250.00},
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


