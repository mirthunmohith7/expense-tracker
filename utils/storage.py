import json
import os
def load_expense():
    if not os.path.exists('data/expenses.json'):
        return []

    try:
        with open('data/expenses.json', 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        return []
def save_expense(expenses):
    with open ('data/expenses.json','w') as f:
        json.dump(expenses,f)