class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"You have successfully deposited ${amount:,.2f}. New balance: ${self.account_balance:,.2f}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Error: Cannot withdraw more than your account balance.")
        else:
            self.account_balance -= amount
            print(f"You have successfully withdrawn ${amount:,.2f}. New balance: ${self.account_balance:,.2f}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:,.2f}")

    def menu(self):
        while True:
            print("\n--- Bank Menu ---")
            print("1. Deposit")
            print("2. Withdraw funds")
            print("3. Display balance")
            print("4. Exit")

            choice = input("Choose an option (1–4): ")

            if choice == "1":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            elif choice == "3":
                self.display_balance()
            
            elif choice == "4":
                print("Thank you for banking with us. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a number between 1 and 4.")


# --- Program starts here ---
account = BankAccount(0)
account.menu()
