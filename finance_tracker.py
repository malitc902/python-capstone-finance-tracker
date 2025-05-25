# Personal Finance Tracker
print("Welcome to the Personal Finance Tracker!")  # Display a welcome message when the program starts

# Dictionary to store expenses by category
expenses = {}  # Initialize an empty dictionary to store expenses, categorized by type

def add_expense():
    """Function to add an expense with description, category, and amount."""
    try:
        # Get user input for expense details
        description = input("Enter expense description: ")  # Description of the expense (string)
        category = input("Enter category: ")  # Category under which the expense falls (string)
        amount = float(input("Enter amount: "))  # Convert input to float for numerical operations
        
        # Ensure the category exists in the dictionary; if not, initialize it
        if category not in expenses:
            expenses[category] = []  # Create an empty list for this category

        # Append the expense as a tuple (description, amount) into the appropriate category
        expenses[category].append((description, amount))  

        print("Expense added successfully!")  # Confirm successful addition
    except ValueError:  
        print("Invalid amount. Please enter a number.")  # Handle non-numeric inputs gracefully

def view_expenses():
    """Function to display all expenses categorized."""
    print("\nExpenses:")  # Print section header

    # Loop through each category in the dictionary
    for category, expense_list in expenses.items():
        print(f"Category: {category}")  # Display category name
        
        # Loop through each expense in the category and display details
        for desc, amt in expense_list:
            print(f"  - {desc}: ${amt:.2f}")  # Format amount to 2 decimal places for readability

def view_summary():
    """Function to display total amount spent per category."""
    print("\nSummary:")  # Print section header
    
    # Iterate through each category in the dictionary
    for category, expense_list in expenses.items():
        total = sum(amt for _, amt in expense_list)  # Sum up all expenses in the category
        print(f"{category}: ${total:.2f}")  # Print category-wise total expenses

# Main loop to keep the program running until user chooses to exit
while True:
    print("\nOptions:")  # Print available menu options
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")
    
    choice = input("Enter your choice: ")  # Ask for user input

    if choice == '1':
        add_expense()  # Call the function to add an expense
    elif choice == '2':
        view_expenses()  # Call the function to display all expenses
    elif choice == '3':
        view_summary()  # Call the function to display expense summary
    elif choice == '4':
        print("Goodbye!")  # Exit message
        break  # Terminate loop and end program
    else:
        print("Invalid choice. Please try again.")  # Handle invalid menu selections