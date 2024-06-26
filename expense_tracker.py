class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.descrition = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses(index)
            print('Expense removed successfully.')
        else:
            print('Invalid expense index.')

    def view_expenses(self, expenses):
        if len(self.expenses) == 0:
            print('No expenses found.')
        else:
            print('Expense list:')
            for i, expense in enumerate(self.expenses, start=1):
                print(f'{i}. Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount:.2f}')

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)    
        print(f'Total amount: ${total:.2f}')