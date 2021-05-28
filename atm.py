import datetime
from random import *
import validation
import database
from getpass import getpass

accountNumberFromUser = None

def init():
    print("Welcome to bankPHP")

    haveAccount = int(input("How can I help you Today: (1) ATM (2) Login (3) Create An Account (4)Exit \n"))

    if(haveAccount == 1):
        atm()

    elif(haveAccount == 2):
        login()

    elif(haveAccount == 3):
        register()

    elif(haveAccount == 4):
        exit()
    else:
        print("You have selected invalid option")
        init()


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
                init()



def login():
    
    print("********* Login ***********")
    global accountNumberFromUser
    accountNumberFromUser = int(input("What is your account number? \n"))

    is_vlid_account_number = validation.account_number_validation(accountNumberFromUser)

    if is_vlid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(accountNumberFromUser, password)

        if user:
            database.login_auth_session(accountNumberFromUser, user)
                           
        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only numbers")
        init()



def register(): 

    print("****** Register ******")

    email = input("Email: \n")
    first_name = input("First Name: \n")
    last_name = input("Last Name: \n")
    password = getpass("create a password: \n")

    accountNumber = generationAccountNumber()

    is_user_created = database.create(accountNumber, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print("== ==== ====== ==== ==")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print("== ==== ====== ==== ==")

        login()

    else:
        print("Something went wrong, please try again")

        register()



def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1]))

    selectedOption = input("Please select an Option: (1) deposit (2) withdrawal (3) Logout (4) Exit \n")

    if(selectedOption == 1):
         depositOperation(user)

    elif(selectedOption == 2):
        withdrawalOperation() 

    elif(selectedOption == 3):
        login()

    elif(selectedOption == 4):
         exit()

    else:
        print("Invalid option selected")
        bankOperation(user)



def withdrawalOperation(user):
   current_balance = int(get_current_balance(user))
   amount_to_withdrawal = int(input("How much do you want to withdrawal"))
   current_balance -= amount_to_withdrawal
   set_current_balance(user, str(current_balance))


   if database.update(accountNumberFromUser, user):
       print("Your account balance is {}".format(current_balance))
       bankOperation(user)
   else:
        print("Transaction not successful")

def depositOperation(user):
   
   current_balance = int(get_current_balance(user))
   amount_to_deposit = int(input("How much do you want to deposit? "))
   current_balance += amount_to_deposit
   set_current_balance(user, str(current_balance))


   if database.update(accountNumberFromUser, user):
       print("Your account balance is {}".format(current_balance))
       bankOperation(user)
   else:
        print("Transaction not successful")


def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def set_current_balance(user_details, balance):
    user_details[4] = balance

def get_current_balance(user_details):
    return user_details[4]

def logut():

    login()

#### ACTUAL BANKING SYSTEM####   
  
init()



