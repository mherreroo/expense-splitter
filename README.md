# Expense Splitter "SplitEasy"
#### Video Demo:  <https://youtu.be/kdWhjrudDl4>

## Description:
The Expense Splitter "SplitEasy" is a Flask web application which simplifies dividing shared expenses across a group of individuals evenly. Restaurant bills, rent, and travel expenses alike, the app simplifies the calculation by figuring out who should pay whom. The app marries backend Python functionality with an interactive frontend created via HTML templates to provide an interactive and functional interface.

## Overview of the Project
Expense Splitter takes user input in the form of names and quantities of expenses, computes these into balances, and displays final amounts owed dynamically on a web page. Flask is the web framework that receives requests, processes users' input, and sends back results through Jinja templating. The calculation offers a convenient and automated method of balancing monetary imbalances among big groups of participants.

## Project File Structure
This is the application's core, where the web frontend and the cost processing backend code are stored. It does the following:

### 1. **project.py** (Backend Logic)
- **Flask Initialization:** The Flask web application is created with `Flask(__name__, template_folder="templates")`, meaning the application runs with HTML files stored in the templates directory.
- **Expense Storage:** The expenses dictionary stores participants and how much they spent.
- **Expense Addition:** The `add_expense(name, amount)` function updates the expenses dictionary when new expenses are added.
- **Calculation of Expense Splits:**
  - The `calculate_splits()` function determines how much money each individual owes or is owed.
  - Computes total expenses and divides the amount equally among participants.
  - Identifies differences between each individual's contribution and the equal share.
- **Flask Route Handling:**
  - `@app.route("/", methods=["GET", "POST"])` manages both the expense submission (via POST requests) and expense balancing (via GET requests).
  - The function `render_template("index.html", balances=balances)` ensures that the calculated balances are dynamically displayed on the webpage.
- **Server Execution:**
  - The script runs the Flask app when executed as the main program using `if __name__ == "__main__": app.run(debug=True)`.  

### 2. **templates/index.html** (Frontend UI)
This is the main user interface built using HTML and Jinja templating. It provides the structure for displaying results and dynamically updating balances.
- **Title and Headings:** Displays "Final Balances" to indicate the calculation results.
- **Jinja Loop to Display Balances:**
  - `{% for name, balance in balances.items() %}` iterates through the balance dictionary and prints relevant messages:
    - If the balance is positive: "[User] should be reimbursed $X.XX"
    - If the balance is negative: "[User] owes $X.XX"
    - If the balance is zero: "[User] is settled up."
- **Expense Form:**
  - Users enter their names and expenses in a simple form that submits data via POST to the Flask application.

### 3. **README.md (Project Documentation)**
This file documents the Expense Splitter project, including:
- Project purpose and objectives
- Installation and setup instructions
- Usage guide
- Future enhancements and features

### 4. **test_project.py (Optional - Testing)**
This file contains test cases to verify the correctness of calculations:
- Ensures that money is split correctly.
- Validates correct balance outputs for various input cases.
- Includes edge cases where all participants spend the same amount.

## How It Works
1. **User Input:** Users enter their names and expenses.
2. **Expense Processing:** The Flask backend processes the data and computes balances.
3. **Balance Calculation:** The script determines who owes whom and how much.
4. **Displaying Results:** The results are dynamically displayed on the webpage, providing a clear summary of the expense split.

## Technologies Used
- **Python**: Manages calculations and Flask backend framework.
- **Flask**: Web framework for request handling and template rendering.
- **HTML + Jinja2**: Provides dynamic UI updates and content rendering.
- **GitHub Codespaces**: Used for cloud-based development and testing.

## Challenges and Solutions
### 1. **Template Not Found Error**
- **Problem:** Flask was unable to locate `index.html`.
- **Solution:** Explicitly set `template_folder="templates"` in Flask initialization.

### 2. **Port 5000 Already in Use**
- **Problem:** The app couldn't restart because another process was using port 5000.
- **Solution:** Identified and terminated the process using `lsof -i :5000` and `kill -9 <PID>`.

### 3. **Handling Zero and Negative Balances**
- **Problem:** Ensuring users who contributed the correct amount do not appear as debtors or creditors.
- **Solution:** Added conditionals to differentiate between debtors, creditors, and settled users.

## Future Improvements
- **User Authentication:** Add login functionality to track user spending.
- **Expense Categories:** Group expenses into categories (e.g., Food, Rent, Travel).
- **Graphical Representation:** Use libraries like Chart.js or D3.js to visualize expense data.
- **Database Integration:** Store expenses persistently in PostgreSQL or SQLite.

## Conclusion
The **Expense Splitter "SplitEasy"** is a practical and user-friendly tool for managing shared expenses. Using Flask and Python, it dynamically computes and distributes financial obligations fairly among users. With the potential for future enhancements, the project demonstrates strong web development and problem-solving skills, making it a useful real-world application to be proud of. 🚀

