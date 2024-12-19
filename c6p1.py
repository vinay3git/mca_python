class BankAccount:
    def __init__(self, name, account_number, account_type, balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def display_details(self):
        print(f"\nAccount Details:")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
def get_account_details():
    name = input("Enter the name of the depositor: ")
    account_number = input("Enter the account number: ")
    account_type = input("Enter the account type (e.g., Savings, Current): ")
    balance = float(input("Enter the initial balance: "))
    return name, account_number, account_type, balance

def main():
    name, account_number, account_type, balance = get_account_details()
    account = BankAccount(name, account_number, account_type, balance)
    account.display_details()
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display account details")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display_details()
        elif choice == 4:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
