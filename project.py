from flask import Flask, render_template, request

# Explicitly specify the templates folder
app = Flask(__name__, template_folder="templates")

# Store expenses in a dictionary
expenses = {}

# Function to add expenses
def add_expense(name, amount):
    if name in expenses:
        expenses[name] += amount
    else:
        expenses[name] = amount

# Function to calculate splits
def calculate_splits():
    total_spent = sum(expenses.values())
    num_people = len(expenses)
    equal_share = total_spent / num_people if num_people > 0 else 0

    balances = {name: round(amount - equal_share, 2) for name, amount in expenses.items()}
    return balances

# Flask Route: Home Page (Form to Input Expenses)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        add_expense(name, amount)

    balances = calculate_splits()
    return render_template("index.html", balances=balances)

if __name__ == "__main__":
    app.run(debug=True)

#ChatGPT has been used through the whole process: OpenAI. (2025). ChatGPT (March 1 version) [Large language model]. https://chatgpt.com 