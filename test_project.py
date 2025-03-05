from project import add_expense, calculate_splits  # Import functions

# Test for add_expense function
def test_add_expense():
    expenses = {}  # Start with an empty dictionary
    add_expense(expenses, "Alice", 50)  # Alice spends $50
    assert expenses["Alice"] == 50  # Check if Alice's amount is stored correctly

    add_expense(expenses, "Alice", 30)  # Alice spends $30 more
    assert expenses["Alice"] == 80  # Now she should have $80 stored

# Test for calculate_splits function
def test_calculate_splits():
    expenses = {"Alice": 60, "Bob": 40}  # Alice spent $60, Bob spent $40
    result = calculate_splits(expenses)  # Calculate balances
    assert result["Alice"] == 10  # Alice overpaid by $10
    assert result["Bob"] == -10  # Bob underpaid by $10

    expenses = {"Charlie": 30, "Dana": 30, "Eve": 30}  # Everyone paid equally
    result = calculate_splits(expenses)
    assert all(balance == 0 for balance in result.values())  # Everyone should be settled

# Since display_results only prints, we don't need to test it

#ChatGPT has been used through the whole process: OpenAI. (2025). ChatGPT (March 1 version) [Large language model]. https://chatgpt.com 