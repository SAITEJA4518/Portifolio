import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, date, family_member):
        self.amount = amount
        self.category = category
        self.date = date
        self.family_member = family_member

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date.strftime('%Y-%m-%d'),
            'family_member': self.family_member
        }

class FamilyExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.family_members = set()

    def add_family_member(self, name):
        self.family_members.add(name)

    def add_expense(self, amount, category, date, family_member):
        if family_member not in self.family_members:
            print(f"Family member '{family_member}' does not exist.")
            return
        expense = Expense(amount, category, date, family_member)
        self.expenses.append(expense)
        print(f"Added expense: {expense.to_dict()}")

    def view_summary(self):
        summary = {}
        for expense in self.expenses:
            if expense.family_member not in summary:
                summary[expense.family_member] = {}
            if expense.category not in summary[expense.family_member]:
                summary[expense.family_member][expense.category] = 0
            summary[expense.family_member][expense.category] += expense.amount
        
        return summary

    def save_expenses(self, filename):
        with open(filename, 'w') as f:
            json.dump([expense.to_dict() for expense in self.expenses], f)
        print("Expenses saved to", filename)

    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as f:
                expenses_data = json.load(f)
                for item in expenses_data:
                    date = datetime.strptime(item['date'], '%Y-%m-%d')
                    expense = Expense(item['amount'], item['category'], date, item['family_member'])
                    self.expenses.append(expense)
                print("Expenses loaded from", filename)
        except FileNotFoundError:
            print("File not found.")

def main():
    tracker = FamilyExpenseTracker()
    
    while True:
        print("\n--- Family Expense Tracker ---")
        print("1. Add Family Member")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save Expenses")
        print("5. Load Expenses")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter family member's name: ")
            tracker.add_family_member(name)

        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                date_input = input("Enter date (YYYY-MM-DD): ")
                date = datetime.strptime(date_input, '%Y-%m-%d')
                family_member = input("Enter family member's name: ")
                tracker.add_expense(amount, category, date, family_member)
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == '3':
            summary = tracker.view_summary()
            print("\n--- Expense Summary ---")
            for member, categories in summary.items():
                print(f"{member}:")
                for category, total in categories.items():
                    print(f"  {category}: ${total:.2f}")

        elif choice == '4':
            filename = input("Enter filename to save expenses: ")
            tracker.save_expenses(filename)

        elif choice == '5':
            filename = input("Enter filename to load expenses: ")
            tracker.load_expenses(filename)

        elif choice == '6':
            print("Exiting the tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
