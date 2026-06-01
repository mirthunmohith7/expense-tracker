# CLI Expense Tracker (Python)

A simple command-line expense tracking application built using Python.  
It demonstrates core programming concepts, file handling, and basic software design principles.

---

## 🚀 Features

- Add expenses with amount, category, and optional description
- View all stored expenses in a formatted table
- Delete expenses by selecting index
- View total spending
- Persistent storage using JSON (data is saved even after program exit)
- Input validation and error handling for safe usage

---

## 🧱 Project Structure
expense-tracker/
│
├── main.py
├── utils/
│ ├── helpers.py
│ └── storage.py
├── data/
│ └── expenses.json
└── README.md

---

## ⚙️ How to Run

Make sure you have Python installed.

Run the program:

```bash
python main.py

💾 Data Storage

All expenses are stored in a local JSON file:

data/expenses.json

This allows data to persist between sessions.

📚 Concepts Used
Python functions
Loops and conditionals
Dictionaries and lists
Input validation
File handling
JSON serialization/deserialization
Modular programming
Basic CLI design

🧠 What I Learned
How to structure a small Python project into modules
How to separate logic (helpers) and storage (file handling)
How to handle invalid user input safely
How persistence works using JSON files
How to design a simple command-line interface
🚧 Future Improvements

Category-wise spending breakdown
Monthly expense tracking
Sorting expenses by amount/date
Export to CSV
Better CLI UI formatting
