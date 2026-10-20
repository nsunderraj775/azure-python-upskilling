from ledger import format_money, classify

amounts = [50, 100, 1000, 2500, 15000]
for amount in amounts:
    print(f"{format_money(amount)} -> {classify(amount)}")


