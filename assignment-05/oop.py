class ATM:
    def __init__(self):
        """
        Here is ATM CODE
        """
        self.pin = "1234"
        self.balance = 2000.0
        self.is_authenticated = False

    def check_pin(self, input_pin):
        "Verify the entered pin"
        if input_pin == self.pin:
            self.is_authenticated = True
            print(" Pin verified successfully\n")
        else:
            print(" Incorrect pin! Please try again\n")

    def check_balance(self):
        """
        Display the current balance if authenticated!
        """
        if self.is_authenticated:
            print(f" Current Balance is: {self.balance:.2f}\n")
        else:
            print(" Please enter the correct pin\n")

    def deposit(self, amount):
        """
        Deposit the specified amount if authenticated and amount is positive
        """ 
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f" {amount:.2f} deposited successfully")
                print(f" New balance is {self.balance:.2f}\n")
            else:
                print(" Deposited amount must be positive\n")
        else:
            print(" Please enter the correct pin\n")

    def with_draw(self, amount):
        """
        Withdraw the specified amount from the account balance
        if sufficient funds are available and user is authenticated.
        """
        if self.is_authenticated:
            if amount > self.balance:
                print(" Insufficient balance.\n")
            elif amount <= 0:
                print(" Withdrawal amount must be positive\n")
            else:
                self.balance -= amount
                print(f"{amount:.2f} withdrawn successfully")
                print(f" Remaining balance: {self.balance:.2f}\n")
        else:
            print(" Please enter the correct pin\n")

    def exit(self):
        """
        Exit the ATM Session
        """
        print(" Thank you for using the ATM machine. Goodbye!")
        return False

    def menu(self):
        """
        Display the menu and handle user interaction
        """
        attempts = 0
        while attempts < 3:
            input_pin = input("🔢 Please enter your 4-digit PIN: ")
            if input_pin == self.pin:
                self.is_authenticated = True
                print(" PIN verified successfully!\n")
                break
            else:
                attempts += 1
                print(f" Incorrect PIN ({attempts}/3)\n")
        if not self.is_authenticated:
            print("🔒 Too many incorrect attempts. Exiting...\n")
            return

        while True:
            print("=== ATM MENU ===")
            print("1: Check Balance")
            print("2: Deposit Money")
            print("3: Withdraw Money")
            print("4: Exit")
            choice = input("Please select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print(" Invalid input! Please enter a numeric value.\n")
            elif choice == "3":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    self.with_draw(amount)
                except ValueError:
                    print(" Invalid input! Please enter a numeric value.\n")
            elif choice == "4":
                if self.exit() == False:
                    break
            else:
                print(" Invalid selection! Please choose a valid option.\n")


if __name__ == "__main__":
    atm = ATM()
    atm.menu()