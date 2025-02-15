# Personal Account Management

## Overview
This project implements a simple personal bank account management system using Python. It includes two classes:
1. `Amount` - Represents individual transactions (deposits and withdrawals).
2. `PersonalAccount` - Represents a bank account, handling deposits, withdrawals, and transaction history.

The project demonstrates object-oriented programming (OOP) principles such as encapsulation, class relationships, and method overloading.

---

## Classes and Methods

### `Amount` Class
**Purpose**: Represents a financial transaction.

**Attributes:**
- `amount` (float): The transaction amount.
- `timestamp` (datetime): The date and time of the transaction.
- `transaction_type` (str): The type of transaction ('DEPOSIT' or 'WITHDRAWAL').

**Methods:**
- `__init__(self, amount, transaction_type)`: Initializes an Amount instance.
- `__str__(self)`: Returns a string representation of the transaction.

---

### `PersonalAccount` Class
**Purpose**: Represents a bank account and manages transactions.

**Attributes:**
- `account_number` (int): Unique identifier for the account.
- `account_holder` (str): The name of the account holder.
- `balance` (float): The current balance in the account.
- `transactions` (list): Stores instances of `Amount` representing transactions.

**Methods:**
- `__init__(self, account_number, account_holder)`: Initializes the account.
- `deposit(self, amount)`: Deposits money into the account.
- `withdraw(self, amount)`: Withdraws money if sufficient balance is available.
- `print_transaction_history(self)`: Prints all transactions.
- `get_balance(self)`: Returns the current balance.
- `get_account_number(self)`: Returns the account number.
- `set_account_number(self, account_number)`: Sets a new account number.
- `get_account_holder(self)`: Returns the account holder's name.
- `set_account_holder(self, account_holder)`: Updates the account holder's name.
- `__str__(self)`: Returns a string representation of the account.
- `__add__(self, amount)`: Allows deposits using `+` operator.
- `__sub__(self, amount)`: Allows withdrawals using `-` operator.

---

## How to Run the Program
### Prerequisites
Ensure you have Python installed (Python 3 recommended).

### Steps
1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Run the script using:
   ```bash
   python bank_account.py
   ```
4. Follow the on-screen instructions to test the functionality.

---

## Test Cases
Ensure that the `PersonalAccount` class functions correctly under various scenarios:
1. **Deposit Scenario**:
   - Deposit `$500`, check if balance updates correctly.
2. **Withdrawal Scenario**:
   - Withdraw `$200`, verify transaction history and balance.
   - Attempt to withdraw more than the balance (should display an error).
3. **Transaction History**:
   - Check if deposits and withdrawals are properly recorded.
4. **Account Details**:
   - Verify account number and holder's name updates.

