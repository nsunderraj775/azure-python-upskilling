p= 20000
annualrate = 0.06
r = annualrate/12
n = 12
balance = p
payment = p * r/(1-(1+r)**-n)
print(f"Payment:${payment:,.2f}")
for month in range(1,13):
 interest = balance * r
 principal_paid = payment - interest
 balance = balance - principal_paid
 print(f"Month {month}: interest ${interest:,.2f} principal ${principal_paid:,.2f} balance ${balance:,.2f}")

  