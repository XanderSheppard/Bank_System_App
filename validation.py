def account_number_validtion(accountNumber):
   
    #if accountNumber is 10 digits
    #if the accountNumber is integer
    if accountNumber:
        
        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True 
            except ValueError:
                print("Invalid Account Number, account number should be numbers")
                return False

        else:
            print("Account Number connot be more or less then 10 digits")
            return False

    else:
        print("Account Number is required")
        return False
