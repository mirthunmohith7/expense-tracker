def display_menu():
    print("1.Add expense\n2.View expenses\n3.Exit")
expenses=[]
def add_expenses(expenses):
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount<=0:
                print("Amount must be greater than 0...")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    category = input("Enter category: ")
    description = input("Enter Description: ")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    print("Expense added succesfully...")
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
    elif choice == 2:
        print("View expenses selected")
        print(expenses)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")