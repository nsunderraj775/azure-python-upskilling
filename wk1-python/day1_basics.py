account_id = "ACC-1001"
balance = 2500.75
num_transactions = 42
is_active = True
print(account_id)
print(balance)
print(num_transactions)
print(is_active)
print(f"Account {account_id} has a balance of ${balance:,.2f}")
deposit = 1200
new_balance = balance + deposit
print(f"After a deposit of ${deposit:,.2f}, the balance is ${new_balance:,.2f}")
