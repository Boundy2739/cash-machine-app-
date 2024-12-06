def view_balance(balance):
    print("Your current balance is £",balance)
def deposit(balance):
    money = int(input("Please insert the amount of money you want to add\n"))
    balance = balance + money
    print("You added £",money," now your current balance is £",balance)
    return balance
def withdraw(balance):
    money = int(input("Please insert the amount of money you want to withdraw"))
    if money > balance:
        print("You don't have enough money to withdraw this amount, your current balance is £",balance)
    else:
        balance = balance - money
        print("You have withdraw £", money,"now your current balance is £",balance)
        return balance



print("Hello world")
username = str(input("create username"))
password = str(input("create password"))
current_bal = int (10)
user_action = 0
print(username, password)

while True:
    user_auth = str(input("Please insert your username"))
    pin_auth = str(input("Please insert your username"))

    if pin_auth == password and user_auth == username:
        print("Access granted\n")
        print("Please choose the action you want to do\n")
        print("Insert 1 if you want to see your current balance\n")
        print("Insert 2 if you want to withdraw money\n")
        print("Insert 3 if you want to deposit money\n")
        print("Insert 4 to view your transaction history\n")
        user_action = int(input("Insert the number for the action you want to do : \n"))
        if user_action == 1:
            view_balance(current_bal)
        if user_action == 3:
            deposit(current_bal)
        if user_action == 2:
            withdraw(current_bal)
            
    else:
        print("Access denied\n")
        print("Please insert the correct credentials\n")
    
