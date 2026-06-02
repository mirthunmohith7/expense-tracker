from utils.storage import load_expense, save_expense
from utils.helpers import view_expenses, add_expenses, delete_expense, total_expenses, category_summary, filter_by_category, monthly_summary
expenses=load_expense()
def display_menu():
    print("1.Add expense\n2.View expenses\n3.Delete\n4.Total\n5.Category Wise Summary\n6.Filter by category\n7.Month wise Summary\n8.Exit")
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
        delete_expense(expenses)
        print("Deleting...")
    elif choice == 4:
        total_expenses(expenses)
    elif choice == 5:
        category_summary(expenses)
    elif choice == 6:
        filter_by_category(expenses)
    elif choice == 7:
        monthly_summary(expenses)
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
    