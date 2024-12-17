from datetime import datetime


def create_pin(): 
    pin = str('') 
    pincheck = 1
    
    #this asks the user to create a pin
    pin = str(input("Create a pin: "))
    
    #the loop checks if the user used the right input, if not they will be asked to do it until they use the right input
    while pincheck == 1:
        
        #this checks if the pin has 4 digits
        if len(pin) == 4:
            try:
                pin = int(pin)
                print(pin)
                pincheck = 0
                print("Pin created!\n")
                return pin
            #this line will be executed if the user has used letters in while creating the pin
            except ValueError:
                print("You need insert 4 digits and no other character\n")
                pin = str(input("Create a pin: "))
        #this will run if the pin does not have exactly 4 digits
        if len(pin) != 4:
             pin = str(input("Please Insert 4 digits number: "))


def initial_balance():
     inputcheck = 1

     #this loop will ask the user to insert an initial balance, if the user uses letters instead of numbers the will be asked to insert again until they get it right
     while inputcheck == 1:
        try:
            balance = float(input("Deposit initial funds : "))
            #this if statement checks if the input is a positive number, if it is negative the user will be asked to put a positive number
            if balance >= 0:
                print("You deposited £",balance)
                inputcheck = 0
                return balance
            else:
                print("Please dont insert a negative value!\n")
        #if the user used letters instead of only numbers, this line will ask them to insert the balance again
        except ValueError:
          print("You need to insert a numeric value!")


def create_account(accounts):
        #this calls the function that creates a pin
        pin = create_pin()
        #this calls the function that assigns an initial balance
        balance = initial_balance()
        #this updates the dictionoary, by adding the pin created and the balance
        accounts.update({pin:balance})
        return accounts
          
#this function prints the available balance
def view_balance(balance):
    print("Your current balance is £",balance)
    return balance
#this functions lets the user deposit money, and writes on a transaction list the amount of money added alongside the date and the time
def deposit(balance):
    #this line gets the current date and time from the local device
    date = datetime.now().replace(second = 0, microsecond=0)
    #this converts the time into a string so it can be written on the transaction text file
    date = str(date)
    inputcheck = 1
    while inputcheck == 1:
        try:
            money = float(input("Please insert the amount of money you want to add: "))
            #this if statement checks if the input is a positive number, if it is negative the user will be asked to put a positive number
            if money >= 0:
                balance = balance + money
                print("You added £",money," now your current balance is £",balance,)
                
                #this converts the money into a string so it can be written on the transction text file
                money = str(money)
                log = open('transactions.txt','a')
                log.write("£")
                log.write(money)
                log.write(" Deposited")
                log.write(" at ")
                log.write(date)
                log.write("\n")
                log.close
        
                return balance
            else:
                print("Please dont insert a negative value\n")
        #this line will be executed in case the user input contains letters
        except ValueError:
             print("You must insert a numeric value!")
        
#this functions lets the user withdraw money, and writes on a transaction list the amount of money taken alongside the date and the time   
def withdraw(balance):
   
    #this line gets the current date and time from the local device
    date = datetime.now().replace(second = 0, microsecond=0)
    #this converts the time into a string so it can be written on the transaction text file
    date = str(date)
    inputcheck = 1
    while inputcheck == 1:
        try:
            
            money = float(input("Please insert the amount of money you want to withdraw: "))
            if money > balance:
                print("You don't have enough funds!\n")
                print("your current balance is £",balance)
            else:
                #this if statement checks if the input is a positive number, if it is negative the user will be asked to put a positive number
                if money >= 0:
                
                    balance = balance - money
                    print("You have withdraw £", money,"now your current balance is £",balance)
                    money = str(money)
                    log = open('transactions.txt','a')
                    log.write("£")
                    log.write(money)
                    log.write(" withdrawn")
                    log.write(" at ")
                    log.write(date)
                    log.write("\n")
                    log.close
                    return balance
                else:
                    print("Please dont use negative values!\n")
        #this line will be executed in case the user input contains letters
        except ValueError:
             print("Please insert numbers only!")

#this function will open the transaction list, read the content and print it for the user
def transactions():
    with open('transactions.txt','r') as log:
        transaction = log.readlines()
        for lines in transaction:
            print(lines)


print("Greetings!")
accounts = {}
ATM = True
accounts_created = 0 
while ATM == True:
    balance = 0
    user_action = 0
    Attempts = 5
    print("Enter 1 to create an account ")
    print("Enter 2 to load an account ")
    print("Enter 3 to exit ")
    try:
        create = int(input("Please choose one of the three options: "))
        if create == 1:
            accounts = create_account(accounts)
            print("Account succefully created!\n")
            #print(accounts)
            accounts_created = accounts_created + 1
            

                
            


            
        if create == 2:
           if accounts_created > 0:

                    
                    while Attempts != 0:
                            
                            #this asks the user to insert a pin
                            try:
                                pin_auth = int(input("Pleas insert your pin : "))
                            #if the pin contains a letter, the user will be asked to insert the pin again
                            except ValueError:
                                print("You must insert a pin!\n")
                            
                        
                            
                            #this for loop will go trough all the keys in the dictionary, and check if there is one that matches with the pin that user as inserted
                            for value in accounts.keys():
                                value = int(value)
                                
                                balance = accounts[value]
                                
                                if value != 0:
                                    
                                    if pin_auth == value:
                                        print("Correct pin")
                                        print("Access granted\n")
                                        login = 1
                                        
                                        while login == 1:    
                                            
                                            
                                            print("Please choose the action you want to do")
                                            print("Enter 1 if you want to see your current balance")
                                            print("Enter 2 if you want to withdraw money")
                                            print("Enter 3 if you want to deposit money")
                                            print("Enter 4 to view your transaction history")
                                            print("Enter 5 to logout\n")
                                            user_action = int(input("Please choose an option : "))
                                            if user_action == 1:
                                                balance = view_balance(balance)
                                                c = input("Do you want to continue? Y/N : ")
                                                c = c.upper()
                                                if c.upper() == 'N':
                                                    input("Have a nice day!")
                                                    exit()
                                                else:
                                                    print("\n")
                                                    print("\n")
                                                   
                                            
                                            if user_action == 3:
                                                balance = float(deposit(balance))
                                                c = input("Do you want to continue? Y/N : ")
                                                c = c.upper()
                                                if c.upper() == 'N':
                                                    input("Have a nice day!")
                                                    exit()
                                                else:
                                                    print("\n")
                                                    print("\n")
                                             
                                            
                                            if user_action == 2:
                                                balance = float(withdraw(balance))
                                                c = input("Do you want to continue? Y/N : ")
                                                c = c.upper()
                                                if c.upper() == 'N':
                                                    input("Have a nice day!")
                                                    exit()
                                                else:
                                                    print("\n")
                                                    print("\n")
                                                    
                                            if user_action == 4:
                                                transactions()
                                                c = input("Do you want to continue? Y/N : ")
                                                c = c.upper()
                                                if c.upper() == 'N':
                                                    input("Have a nice day!")
                                                    exit()
                                                else:
                                                    print("\n")
                                                    print("\n")
                                                   
                                            if user_action == 5:
                                                login = 0
                                                #this changes the initial balance of the account with the new balance after the transactions before logging out
                                                accounts[value] = balance
                                                break
                                if pin_auth == value:
                                    Attempts = 0
                                    print("You have logged out!")
                                    break
                                
                            #if the pin is wrong this if statement will decrease the amount of remaining attempts
                            if  pin_auth != value:
                                print(pin_auth)
                                Attempts = Attempts - 1
                                print("Wrong pin, access denied\n")
                                print(Attempts," attempts left \n")
                                        #if the user runs out of attempts the program will close
                                if Attempts == 0:
                                    input("You have failed too many attempts!")
                                    exit()
                                
                                
             
           else:
               print("You need to create at leas one account\n ")
        if create == 3:
            input("Goodbye!")
            exit()
    #this runs if the user used letters in the pin
    except ValueError:
       print ("Invalid input, please use only numbers!")

    
