class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account"""
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}")

    def display_balance(self):
        """Display the current balance"""
        print(f"Current Balance: ${self.balance}")

    def menu(self):
        """Interactive bank menu"""
        while True:
            print("\n--- Bank Menu ---")
            print("1. Deposit")
            print("2. Withdraw funds")
            print("3. Display balance")
            print("4. Exit")

            choice = input("Choose an option (1–4): ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == "3":
                self.display_balance()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")


# ✅ For testing or manual use:
if __name__ == "__main__":
    account = BankAccount(0)
    # Uncomment one of these two options depending on what you need

    # 1️⃣ For automated test (expected output only)
    # account.deposit(67.0)

    # 2️⃣ For full interactive mode
    account.menu()
