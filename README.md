# CLI Expense Tracker (Python)

A command-line expense tracking application built with Python. This project focuses on building real-world software engineering fundamentals such as modular design, file handling, JSON persistence, input validation, and basic data analysis.

---

## 🚀 Features

- Add expenses with amount, category, and optional description
- View all expenses in a clean formatted table
- Delete expenses using index-based selection
- Calculate total spending
- Persistent storage using JSON (data survives restarts)
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

Make sure Python 3 is installed on your system.

Run the application: 

```bash
python main.py
```
---

💾 Data Storage

All expense data is stored locally in a JSON file:

data/expenses.json

The application automatically loads data on startup and saves updates after changes like adding or deleting expenses.

📊 Example Output
```bash
1. Food        | Rs.250.00 | Lunch
2. Travel      | Rs.100.00 | Metro
3. Shopping    | Rs.999.00 | Shoes
```

📚 Concepts Used
- Python functions and modular programming
- Loops and conditionals
- Lists and dictionaries
- Input validation using try/except
- File handling (open/read/write)
- JSON serialization and deserialization
- Basic CLI (Command Line Interface) design
- Data persistence
- Simple analytics (total spending)

🧠 What This Project Demonstrates

This project is not just a beginner script. It demonstrates:

- Ability to structure a multi-file Python project
- Understanding of separation of concerns (main, logic, storage)
- Handling real-world edge cases like invalid input and missing files
- Working with persistent data storage
- Building maintainable and extensible CLI applications

🚧 Future Improvements
- Category-wise spending breakdown
- Monthly expense tracking
- Sorting expenses by amount and category
- Export data to CSV
- Improved CLI UI formatting
- Search and filter functionality

📌 Status

Actively developed as part of learning software engineering fundamentals and building production-style Python CLI applications.
