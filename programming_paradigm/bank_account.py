class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def menu(self):
        while True:
            print("\n--- Bank Menu ---")
            print("1. Deposit")
            print("2. Withdraw funds")
            print("3. Current balance")
            print("4. Exit")

            choice = input("Choose an option 1-4: ")

            if choice == "1":
                amount = float(input("Enter an amount to deposit: "))
                self.account_balance += amount
                print(f"You have successfully added {amount:,.2f} to your account. "
                      f"New account balance is {self.account_balance:,.2f}")

            elif choice == "2":
                amount = float(input("Enter an amount to withdraw: "))
                try:
                    if amount > self.account_balance:
                        raise ValueError("Insufficient funds")
                except ValueError:
                    print("Error: Cannot withdraw more than account balance.")
                else:
                    self.account_balance -= amount
                    print(f"You have successfully withdrawn {amount:,.2f}. "
                          f"Your new account balance is {self.account_balance:,.2f}")

            elif choice == "3":
                print(f"Current Balance: ${self.account_balance:,.2f}")

            elif choice == "4":
                print("Thank you for banking with us.")
                break

            else:
                print("Invalid choice. Please choose 1–4.")


# Create account and start the menu
account = BankAccount(0)
account.menu()
