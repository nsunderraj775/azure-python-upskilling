amounts = [120.50,2500.00,45.99,980.00,15000.00]
print(amounts)
print(amounts[0])
print(amounts[4])
print(amounts[-1])
print(len(amounts))
print(sum(amounts))
amounts.append(310.00)
print(amounts[4])
print(amounts[-1])
for amount in amounts:
    if amount > 1000:
        print(f"Large transaction: ${amount:,.2f}")