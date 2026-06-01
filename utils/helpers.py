def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses, start=1):
            if not expense['description']: 
                display_text = "No description provided"
            else:
                display_text=expense['description']
            print(f"{index}. {expense['category']:<12} | Rs.{expense['amount']:<10.2f} | {display_text}")
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
    description = input("Enter Description: ").strip()
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    