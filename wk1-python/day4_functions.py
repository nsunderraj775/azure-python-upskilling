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

def classify(amount):   
    if (amount < 100 ) :
        return "Small"
    elif (amount >=100 and amount <= 1000):
        return "Medium"      
    elif (amount >= 1000):
        return "Large"
print(classify(50))
print(classify(100))
print(classify(1000))
print(classify(2500))
def compound_interest(principal, annual_rate, years, compounds_per_year=12):
    return principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)

print(format_money(compound_interest(10000, 0.05, 10)))
print(format_money(compound_interest(10000, 0.05, 10, 1)))
def monthly_payment(principal, annual_rate, months =60):
    r = annual_rate / 12
    n = months  
    M = principal * r / (1 -(1 + r)** -n)
    return M
print(format_money(monthly_payment(20000, 0.06, 12)))
print(format_money(monthly_payment(30000, 0.07, 60)))