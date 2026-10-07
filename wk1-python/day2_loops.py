for month in range(1,13):
    print(f"Month {month}")
balance = 0  
for month in range(1,13):
    balance = balance + 100
    print(f"Month {month}: balance ${balance:,.2f}")
savings = 0
months  = 0
while savings < 5000:
    savings = savings + 100
    months = months + 1
print(f"Months: {months} savings ${savings:,.2f}")