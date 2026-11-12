# ATM Simulation By Dev_Shanzail

class ATM:
    def __init__(self,initial_balance = 0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            return False, "Invalid amount"
        self.balance += amount  
        return True, "Deposit successful"
    
    def withdraw(self,amount):
        if amount <= 0:
            return False, "Invalid amount"
        
        if amount > self.balance:
            return False, "Insufficient funds"
        
        self.balance -= amount
        return True , "Withdrawal successful"
    

class ATMController:
    def __init__(self,atm):
        self.atm = atm

    def get_amount(self):
        while True:
            user = input("Enter a Amount: ")

            try:
                convert = int(user)
                return convert
            except ValueError:
                print("Invalid input, enter digits only")
    

    def show_menu(self):
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")    

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                print(f"Your balance: {self.atm.check_balance()}")
            elif choice == "2":
                amount = self.get_amount()
                success, message = self.atm.deposit(amount)
                print(message)
            elif choice == "3":
                amount = self.get_amount()
                success, message = self.atm.withdraw(amount)
                print(message)
            elif choice == "4":
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice, enter 1 to 4")



def main():
    atm = ATM(initial_balance=0)
    controller = ATMController(atm)
    controller.run()

if __name__ == "__main__":
    main()