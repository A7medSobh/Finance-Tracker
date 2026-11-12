from flask import Flask, render_template, request, redirect
from database.db import create_table, insertTransaction, getTransaction, deleteTransaction

app = Flask(__name__)

# initialize database
create_table()


#Flask routes that recieves the request from the websites
#and calls functions
@app.route("/")
def home():
    transactions = getTransaction()
    return render_template("index.html", transactions=transactions)


@app.route("/add_transaction", methods=["POST"])
def add_transaction():

    description = request.form["description"]
    amount = float(request.form["amount"])
    category = request.form["category"]
    type = request.form["type"]
    date = request.form["date"]
    insertTransaction(description, amount, category, type, date)

    return redirect("/")


@app.route("/delete_transaction/<int:transactionID>", methods=["POST"])
def delete_transaction(transactionID):

    deleteTransaction(transactionID)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
