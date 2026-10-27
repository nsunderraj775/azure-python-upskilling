
from ledger import format_money
from flask import Flask,render_template

app = Flask(__name__)
HIGH_RISK_COUNTRIES = {"IR", "KP", "SY"}
transaction = ([
{"id": 101, "customer": "C001", "amount":  2500.00, "country": "US", "type": "wire"},
{"id": 102, "customer": "C002", "amount": 15000.00, "country": "US", "type": "cash"},
{"id": 103, "customer": "C003", "amount":  9500.00, "country": "US", "type": "cash"},
{"id": 104, "customer": "C001", "amount":   450.75, "country": "GB", "type": "card"},
{"id": 105, "customer": "C004", "amount": 72000.00, "country": "IR", "type": "wire"},
{"id": 106, "customer": "C002", "amount":  9900.00, "country": "US", "type": "cash"},
{"id": 107, "customer": "C005", "amount": 10900.00, "country": "KP", "type": "cash"},


])

def is_ctr(txn):
    if txn["amount"] > 10000 and txn["type"] =="cash":
        return True
    else:
        return False

def is_structuring(txn):
    if txn["amount"] >= 9000 and txn["amount"] <= 10000 and txn["type"] == "cash":
        return True
    else:
        return False
    
def is_highrisk(txn):
    if txn["country"] in HIGH_RISK_COUNTRIES:
        return True
    else:
        return False
    
    
@app.route("/")
def home():
    return "Hello from the AML Transaction Monitor!"

@app.route("/about")
def about():
    return "Built by Sunderraj with Python and Flask."

@app.route("/transactions")
def transactions():
    return render_template("transactions.html",transactions=transaction,format_money = format_money,is_ctr=is_ctr,is_structuring=is_structuring,is_highrisk=is_highrisk)

if __name__ == "__main__":
    app.run(debug=True)



    
    



