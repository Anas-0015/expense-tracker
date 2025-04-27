import matplotlib.pyplot as plt
import datetime
import csv

FILENAME = "expenses.csv"  # Corrected filename

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    category = input("Enter the category: ")
    if not category:
        print("Category cannot be empty!")
        return

    description = input("Enter the description: ")

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

def view_expense():
    print("\n--- All Expenses ---")
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Amount: ${float(row[1]):.2f}, Category: {row[2]}, Description: {row[3]}")
    except FileNotFoundError:
        print("No expenses found yet. Add your first expense!\n")

def show_summary():
    print("\n--- Summary ---")
    total_expenses = 0
    categories = {}

    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[1])
                category = row[2]
                total_expenses += amount
                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

        print(f"Total Expenses: ${total_expenses:.2f}")
        print("Expenses by Category:")
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")

        if categories:
            labels = categories.keys()
            values = categories.values()
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title('Expenses by Category')
            plt.axis('equal')
            plt.show()

    except FileNotFoundError:
        print("No expenses found yet. Add your first expense!\n")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
