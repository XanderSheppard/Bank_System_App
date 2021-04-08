import datetime
import random



database = {} #dictionary



def init():

    isValidOptionSelected = False
    print("Welcome to bankPHP")

    while isValidOptionSelected == False:
        haveAccount = int(input("How can I help you Today: (1) ATM (2) Login (3) Create An Account (4)Exit \n"))

        if(haveAccount == 1):
            isValidOptionSelected = True
            atm()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 3):
             isValidOptionSelected = True
             register()
        elif(haveAccount == 4):
            exit()
        else:
            print("You have selected invalid option")



def atm():
    print("******** ATM ********")

    username = input("What is your username?\n")
    allowedUsers = ['Xander','Gabrielle','Tray']
    allowedPassword = ['Password1','Password2','Password3']
    time = datetime.datetime.now()

    print(allowedUsers.index('Xander'))

    if(username in allowedUsers):
        password = password = input("Your password?\n")
        userId = allowedUsers.index(username)

        if(password == allowedPassword[userId]):

            print('Welcome %s' % username, time)
            
            print('These are the available options')
            print('1. Withdrawal')
            print('2. Cash Deposit') 
            print('3. Complaint')

            selectedOption = int(input("Please select an option: "))

            if(selectedOption == 1):
                print('you selected %s' % selectedOption)
                print(input('How much would you like to withdraw?: '))
                print('please take your cash')
            elif(selectedOption == 2):
                print('you selected %s' % selectedOption)
                amount = input(' How much would you like to deposit?: ')
                print("your current balance", amount)
            elif(selectedOption == 3):
                print('you selected %s' % selectedOption)
                print(input('What issue will you like to report?: '))
                print( "Thank you for contacting us")



def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                           
    print('Invalid account or password')
    login()



def register():

    print("****Register****")

    email = input("Email: \n")
    first_name = input("First Name: \n")
    last_name = input("Last Name: \n")
    password = input("create a password: \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password ]

    print("Your Account Has been created")
    print("== ==== ====== ==== ==")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ====== ==== ==")

    login()



def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1]))

    selectedOption = input("Please select an Option: (1) deposit (2) withdrawal (3) Logout (4) Exit \n")

    if(selectedOption == 1):
         depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation() 

    elif(selectedOption == 3):
        login()

    elif(selectedOption == 4):
         exit()

    else:
        print("Invalid option selected")



def withdrawalOperation():
    print("withdrawal")


def depositOperation():
    print("Deposit")



def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def logut():
    login()

#### ACTUAL BANKING SYSTEM####   
  
init()



