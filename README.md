# CLI Expense Tracker (Python)

A modular command-line expense tracking application built with Python.
This project was developed to practice real-world software engineering fundamentals including data persistence, modular architecture, input validation, JSON handling, analytics features, and Git/GitHub workflows.

---

## 🚀 Features

### Expense Management

* Add new expenses with:

  * Amount
  * Category
  * Optional description
  * Auto-generated date
* View all expenses in a formatted table
* Delete expenses using indexed selection

### Data Persistence

* Save expenses to a JSON file
* Automatically load saved expenses on startup
* Handles missing or corrupted JSON files safely

### Analytics & Filtering

* Calculate total spending
* Category-wise expense summary
* Monthly expense summary
* Filter expenses by category

### Data Validation

* Prevents invalid numeric input
* Rejects zero or negative expense amounts
* Prevents empty categories
* Normalizes category names for consistency

---

## 🧱 Project Structure

```text
expense-tracker/
│
├── main.py
│
├── utils/
│   ├── helpers.py
│   └── storage.py
│
├── data/
│   └── expenses.json
│
├── README.md
└── .gitignore
```

---

## ⚙️ How to Run

Make sure Python 3 is installed.

Run the application:

```bash
python main.py
```

---

## 📦 Technologies Used

* Python 3
* JSON
* Git & GitHub

---

## 💾 Data Storage

All expenses are stored locally in:

```text
data/expenses.json
```

Each expense follows this structure:

```json
{
    "date": "2026-06-02",
    "amount": 250.0,
    "category": "Food",
    "description": "Lunch"
}
```

---

## 📊 Example Output

```text
1. 2026-06-02 | Food        | Rs.250.00    | Lunch
2. 2026-06-02 | Travel      | Rs.100.00    | Metro
3. 2026-06-03 | Shopping    | Rs.999.00    | Shoes
```

### Category Summary

```text
Food        | Rs.1250.00
Travel      | Rs.400.00
Shopping    | Rs.999.00
```

### Monthly Summary

```text
2026-05     | Rs.2000.00
2026-06     | Rs.3500.00
```

---

## 📚 Concepts Practiced

### Python Fundamentals

* Functions
* Loops
* Conditionals
* Lists & dictionaries
* String formatting
* Exception handling

### Software Engineering Concepts

* Modular project architecture
* Separation of concerns
* Input validation
* Data normalization
* Persistent storage
* Aggregation & analytics logic
* Iterative development
* Defensive programming

### Git & GitHub

* Repository initialization
* Commits & version control
* Branch management
* Remote repositories
* GitHub project publishing

---

## 🧠 What This Project Demonstrates

This project focuses on building practical engineering habits rather than only learning syntax.

It demonstrates:

* Building a multi-file Python application
* Structuring reusable modules
* Handling real-world edge cases
* Designing maintainable CLI applications
* Working with persistent data
* Implementing analytics features using dictionaries and aggregation logic

---

## 🚧 Possible Future Improvements

* Sort expenses by amount/date
* Export expenses to CSV
* Expense search functionality
* Budget limits and alerts
* SQLite database integration
* Flask web version of the application
* User authentication system
* Charts and spending visualization

---

## 📌 Project Status

Version: `v1.0`

Completed as a foundational software engineering project while learning Python, Git, GitHub, and backend development concepts.
