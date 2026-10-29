import csv  
from ledger import format_money
from flask import Flask,render_template

app = Flask(__name__)
HIGH_RISK_COUNTRIES = {"IR", "KP", "SY"}

def load_transactions():
    newlist  = []
    rejected = []
    with open("transactions.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["amount"] = float(row["amount"])
                newlist.append(row)
            except ValueError:
                                print(f"DQ warning: transaction {row['id']} has invalid amount {row['amount']} - skipped")
                                rejected.append(row) 
        return newlist,rejected                                                                                         

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
     good, bad = load_transactions()
     return render_template("transactions.html",transactions=good,rejected=bad,format_money = format_money,is_ctr=is_ctr,is_structuring=is_structuring,is_highrisk=is_highrisk)

if __name__ == "__main__":
    app.run(debug=True)





    
    



