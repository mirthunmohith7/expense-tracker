from utils.storage import load_expense, save_expense
from utils.helpers import view_expenses, add_expenses
expenses=load_expense()
def display_menu():
    print("1.Add expense\n2.View expenses\n3.Exit")
while True:
    try:
        display_menu()
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        print("Add expense selected")
        add_expenses(expenses)
        save_expense(expenses)
    elif choice == 2:
        print("View expenses selected")
        view_expenses(expenses)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
    