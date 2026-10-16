transactions = [
    {"id": 101, "customer": "C01", "country": "US", "type": "purchase", "amount": 120.00},
    {"id": 102, "customer": "C02", "country": "US", "type": "atm",      "amount": 400.00},
    {"id": 103, "customer": "C01", "country": "ZZ", "type": "transfer", "amount": 9500.00},
    {"id": 104, "customer": "C03", "country": "US", "type": "purchase", "amount": 65.50},
    {"id": 105, "customer": "C02", "country": "CA", "type": "transfer", "amount": 12000.00},
    {"id": 106, "customer": "C01", "country": "US", "type": "atm",      "amount": 300.00},
    {"id": 107, "customer": "C04", "country": "US", "type": "purchase", "amount": 2500.00},
    {"id": 108, "customer": "C03", "country": "ZZ", "type": "transfer", "amount": 9800.00},
    {"id": 109, "customer": "C04", "country": "US", "type": "transfer", "amount": 50.00},
    {"id": 110, "customer": "C01", "country": "ZZ", "type": "purchase", "amount": 75.00},
]
high_risk_countries = ["ZZ"]

##“this is the dictionary”
custtotals = {}
##“the for loop for the transactions list”
for txn in transactions:
##txn holds one whole row (id, customer, country, type, amount), not all the customers.
##This line pulls this row’s customer ID (e.g. "C01") out into customer
    customer = txn["customer"] 
##custtotals[customer] holds that customer’s running total. The line means 
##get their total so far (0 the first time), add this row’s amount, and store it back
    custtotals[customer] = custtotals.get(customer,0) + txn["amount"]
##“loop for customer and amount”
for customer,totals in custtotals.items():
##“printing the customer and amount    
    print(f"{customer}: ${totals:,.2f}")
#  empty dictionary: count of transactions per type
counttype = {} 
## for loop for the transactions
for txn in transactions: 
    # txn is one transaction (one row); get its type, e.g. "purchase"
    txn_type = txn["type"]
    # add 1 to the running count for this sustomer type
    counttype[txn_type] =  counttype.get(txn_type,0) + 1 
# loop over each type and its count
for txn_type,counts in counttype.items():   
    # print each type and its count
    print(f"{txn_type}: {counts}")
greater = [txn['id'] for txn in transactions if txn['amount'] > 10000 ]
print(f"transaction ids greater than 10000: {greater}")

rangeamount = [txn['id'] for txn in transactions if txn['amount']< 10000  and txn['amount']>= 9000 and txn['type'] == "transfer"]
print(f"Find the transfer type for the ids range less 10000: {rangeamount}")
highrisk = {txn['customer'] for txn in transactions  if txn['country'] in  high_risk_countries}
print(f"cusotmer id for the high risk countries: {highrisk}")
top_amount = max(custtotals.values())
top_customers = [customer for customer, amount in custtotals.items() if amount == top_amount]
print(f"Top Customer: {top_customers} with ${top_amount:,.2f}")