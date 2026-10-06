balance = 500
withdrawal = 750

if withdrawal <= balance:
    print("Approved")
    balance = balance - withdrawal
else:
    print("Declined: insufficient funds")

print(f"Balance: ${balance:,.2f}")