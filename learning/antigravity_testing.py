class BankAccount:
    """A simple bank account using OOP concepts."""

    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def credit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("Credit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"₹{amount} credited successfully.")

    def debit(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Debit amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
            return
        self.balance -= amount
        print(f"₹{amount} debited successfully.")

    def show_balance(self):
        """Display the current account balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


class Bank:
    """A simple bank system that manages multiple accounts."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
            return None

        account = BankAccount(account_holder, account_number, initial_balance)
        self.accounts[account_number] = account
        print(f"Account created for {account_holder} successfully.")
        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return

        for account in self.accounts.values():
            account.show_balance()
            print("-" * 20)


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Credit Amount")
        print("3. Debit Amount")
        print("4. Show Balance")
        print("5. View All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            acc_no = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(name, acc_no, balance)

        elif choice == "2":
            acc_no = input("Enter account number: ")
            account = bank.find_account(acc_no)
            if account:
                amount = float(input("Enter amount to credit: "))
                account.credit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc_no = input("Enter account number: ")
            account = bank.find_account(acc_no)
            if account:
                amount = float(input("Enter amount to debit: "))
                account.debit(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_no = input("Enter account number: ")
            account = bank.find_account(acc_no)
            if account:
                account.show_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            bank.display_all_accounts()

        elif choice == "6":
            print("Thank you for using the banking system!")
            break

        else:
            print("Invalid choice. Please try again.")
