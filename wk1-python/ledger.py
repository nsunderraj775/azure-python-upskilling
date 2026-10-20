def format_money(amount):
    return f"${amount:,.2f}"
  
def monthly_payment(principal, annual_rate, months =60):
        r = annual_rate / 12
        n = months  
        M = principal * r / (1 -(1 + r)** -n)
        return M
def classify(amount):   
    if (amount < 100 ) :
        return "Small"
    elif (amount >=100 and amount <= 1000):
        return "Medium"      
    elif (amount >= 1000):
        return "Large"

def compound_interest(principal, annual_rate, years, compounds_per_year=12):
    return principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)



