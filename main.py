from amount import PersonalAccount
def main():
    account = PersonalAccount(123456, "Nursezim Alieva")
    print(account)

    account.deposit(500)
    print(f"Balance after deposit: ${account.get_balance():.2f}")

    account.withdraw(200)
    print(f"Balance after withdrawal: ${account.get_balance():.2f}")\

    account.print_transaction_history()

if __name__ == "__main__":
    main()