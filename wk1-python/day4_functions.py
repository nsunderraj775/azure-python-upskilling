def format_money(amount):
    return f"${amount:,.2f}"

print(format_money(5700))
print(format_money(89.5))
print(format_money(12400))

def show_money(amount):
    print(f"${amount:,.2f}")

result = show_money(5700)
print(result)
Amount = 15000
if Amount < 100: 
 print("Small")
elif  Amount <= 1000:
 print("Medium")
else:
 print ("Large")
if Amount >= 10000:
 print("Flag for review: currency transaction report threshold")