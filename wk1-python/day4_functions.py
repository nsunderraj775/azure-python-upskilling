def format_money(amount):
    return f"${amount:,.2f}"

print(format_money(5700))
print(format_money(89.5))
print(format_money(12400))

def show_money(amount):
    print(f"${amount:,.2f}")

result = show_money(5700)
print(result)