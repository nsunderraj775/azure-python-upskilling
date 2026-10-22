from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the AML Transaction Monitor!"
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the AML Transaction Monitor!"

@app.route("/about")
def about():
    return "Built by Sunderraj with Python and Flask."
 

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)