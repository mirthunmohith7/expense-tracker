import json
import os
def load_expense():
    if not os.path.exists('data/expenses.json'):
        return []

    with open('data/expenses.json', 'r') as f:
        return json.load(f)
def save_expense(expenses):
    with open ('data/expenses.json','w') as f:
        json.dump(expenses,f)