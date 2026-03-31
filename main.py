import csv
from datetime import datetime

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.")

def total_expense():
    total = 0
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print("Total Expense:", total)
    except:
        print("No data available.")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
