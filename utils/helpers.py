from datetime import datetime
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses, start=1):
            if not expense['description']: 
                display_text = "No description provided"
            else:
                display_text=expense['description']
            print(f"{index}. {expense['date']:<12} | {expense['category']:<12} | Rs.{expense['amount']:<10.2f} | {display_text}")
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
    while True:
        category = input("Enter category: ").strip().title()
        if not category:
            print("Category cannot be empty")
        else:
            break
    description = input("Enter Description: ").strip()
    date=datetime.now().strftime("%Y-%m-%d")
    expense = {"date": date,"amount": amount, "category": category, "description": description}
    expenses.append(expense)
def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} | Rs.{exp['amount']:.2f} | {exp['description']}")

    while True:
        try:
            choice = int(input("Enter number to delete: "))

            if choice <= 0 or choice > len(expenses):
                print("Invalid number. Try again.")
                continue

            index = choice - 1
            removed = expenses.pop(index)
            print(f"Deleted: {removed['category']} | Rs.{removed['amount']:.2f}")
            break

        except ValueError:
            print("Enter a valid number.")

def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense['amount']

    print(f"Total spending: Rs.{total:.2f}")  

def category_summary(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] +=  amount
        else:
            category_totals[category] =  amount
    for category, total in category_totals.items():
        print(f"{category:<12} | Rs.{total:.2f}")

def filter_by_category(expenses):
    category=input("Enter category name: ").strip().title()
    found=False
    for expense in expenses:
        if expense['category'] == category:
            print(f"{expense['category']:<10} | {expense['amount']:>12.2f} | {expense['description']}")
            found=True
    if not found:
        print("No expenses found for this category")    

def monthly_summary(expenses):
    monthly_totals = {}
    for expense in expenses:
        month = expense['date'][:7]
        amount = expense['amount']
        if month in monthly_totals:
            monthly_totals[month]+= amount
        else:
            monthly_totals[month]= amount
    for month,total in monthly_totals.items():
        print(f"{month:<12} | Rs.{total:.2f}")

