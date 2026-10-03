principal = 10000
annual_rate = 0.05
compounds_per_year = 1
t = 10
A = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * t)

print(f"Final amount ${A:,.2f}")
Interest_earned = A - principal
print(f"Interest ${Interest_earned:,.2f}")