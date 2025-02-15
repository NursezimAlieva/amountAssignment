from datetime import datetime

class Amount:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type
    def __str__(self):
        return f"{self.transaction_type}: ${self.amount:.2f} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount:float):
        if amount > 0:
            transaction = Amount(amount, 'DEPOSIT')
            self.transactions.append(transaction)
            self.balance += amount

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            transaction = Amount(amount, 'WITHDRAWAL')
            self.transactions.append(transaction)
            self.balance -= amount
        else:
            print('Insufficient balance or invalid withdrawal amount')

    def print_transaction_history(self):
        print(f"Transaction History for {self.account_holder} (Account: {self.amount_number})")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number} | Holder: {self.account_holder} | Balance: ${self.balance:.2f}"

    def __add__(self, amount: float):
        self.deposit(amount)
        return self

    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self