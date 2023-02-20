class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


#  Input how many deposits, withdraws and assigned account number
class BankAccount(User):
    total_deposits = 0
    total_withdraws = 0
    accountNumber = "2001009003"

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def retrieveBalance(self):
        #Return the current balance.
        return f"{self.name}, you have a balance of: ${self.balance}"

    #Create deposit Method. Add the amount to the balance + return the new total balance.
    def deposit(self):
    
        try:
            depositFunds = float(input("How much would you like to deposit? "))
            print("Thank you for your deposit.")
            self.balance += depositFunds
            self.total_deposits += 1
            return f"Your balance is now: ${round(self.balance, 2)}."
        except ValueError:
            print("Please input a numerical value.")

    #Create withdraw Method. Subtract the amount from the balance and return the new balance.
    def withdraw(self):

        try:
            amountWithdraw = float(input("How much would you like to withdraw? "))
            print("Thank you for your withdrawal.")
            if amountWithdraw > self.balance:
                print(f"We're sorry, {name} you do not have sufficient funds.\nYour balance is ${self.balance}.")
            else:

                print("Thank you for your business")
                self.balance -= amountWithdraw
                self.total_withdraws += 1
                return f"Your balance is now: ${round(self.balance, 2)}."
        except ValueError:
            print("Please input a numerical value.")

#Give the user 6 options to choose between and add in a catch for other options
def options():
    print("Thank you for logging in to your Deutsche Bank account! Your account number is: " + BankAccount.accountNumber)
    print("Here are a list of options, please choose a number for the option you want: ")
    while True:
        option_choice = int(input(
            "1) See Total Balance\n2) Withdraw Funds\n3) Deposit Funds\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
        if option_choice == 1:
            print(user_one_bank.retrieveBalance())
        elif option_choice == 2:
            print(user_one_bank.withdraw())
        elif option_choice == 3:
            print(user_one_bank.deposit())
        elif option_choice == 4:
            print(f"There have been {user_one_bank.total_withdraws} withdraws")
        elif option_choice == 5:
            print(f"There have been {user_one_bank.total_deposits} deposits")
        elif option_choice == 6:
            print("Thank you for using Deutsche Bank.")
            return False
        else:
            print("Please choose a number between 1-6.")


def bank_creation():
    #starting total balance
    balance = float(0)
    return balance


#   a loop of driver code to execute, then exit to the options function.
while True:
    print("Welcome to Deutsche Bank!")
    name = input("Enter your name: ")
    age = int(input("Enter your current age: "))

    current_user = User(name, age)
    if age >= int(116):
        print("Nobody in our system is this old. Fake user. Have a good day!")
        break
    else:
        print("Thank you",name,"for logging into your account.")
    current_user_balance = bank_creation()
    user_one_bank = BankAccount(current_user.name, current_user.age, current_user_balance)
#Augusta Holtz is the oldest living German man. Cruise is the creator of the application. Allows special notification given specific parameters
    if name == "Augusta Holtz" and age == int(115):
        print("Welcome Augusta Holtz! You are our oldest member at age 115!")
    flag = options()
    if flag == False:
        break
