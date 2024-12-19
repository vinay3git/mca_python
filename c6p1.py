class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def display_details(self):
        print(f"Name: {self.name}, Account: {self.account_number}, Balance: {self.balance}")

def main():
    name = input("Enter the depositor's name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    
    account = BankAccount(name, account_number, balance)
    account.display_details()

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Display details\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_details()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
