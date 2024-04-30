import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'coolbank', password = 'Basketballrocks123')

cursor = connection.cursor()
#this is going to take the account number and put it into a variable from my data. 
accnumber = ('SELECT customeraccnumber FROM coolbank.customerinformation')
#this is going to take the pin number and put it into a variable from my data. 

pinnumber = ('SELECT customerpin FROM coolbank.customerinformation')
#this is going to take the balance and put it into a variable from my data. 

accbalance = ('SELECT customerbalance FROM coolbank.balancesheet')
#this will ask the user their pin and acc number. 
accnumberinput = input("What is your account number: ")
pinnumberinput = input("What is your pin number: ")
#will take information from the customers information from our coolbank. 
customeraccount = ('SELECT accountinformation FROM coolbank.customeraccount')
#this if statement logs the user in to be able to use the functions. If their account number and pin number matches our data, they are allowed to go further into our options. 


def accountchanges():
    #simply goes through and asks the user what changes they'd like to make. 
    accountquestion  = input("Welcome to our account services. What would you like to do? To create a new account, type 1, to discontinue an account or permanently delete it, type 2, and or to change information, type 3. Enter numerical value here:")
    if accountquestion == 1:
        #goes through and takes the information from the user to create a new account. 
        DOBacc = (input("What is your DOB? Enter in a 00/00/0000 value"))
        SSacc =  (input("What is your social security number? Enter as a 000-00-0000"))
        PINacc = (input("What would you like your account pin to be? Enter a three digit pin:"))
        #this creates a new account. 
        newaccountinformation = ("INSERT INTO newaccountinformation (dob, ss, pin) VALUES (DOBacc, SSacc, PINacc)")
    elif accountquestion == 2:
        accountNumber = input("Please confirm your account number. Enter here:")
        #this function checks to see if they would like to delete their account. 
        pinNumber = input("Please confirm your pin number. Enter here")
        if accountNumber == accnumberinput:
            confirmation = input("Are you sure you wish to delete your account?")
            if confirmation == "Yes" or 'yes':
                #if their answer is yes, their information gets deleted from the coolbank account. 
                accnumberinput = ("DELETE accountinformation FROM coolbank")
                print("You have deleted your account with CoolBank. We wish you a good day.")
    elif accountquestion == 3:
        #if the user wishes to modify their existing data, this function will do exactly that. 
        modifyaccount = input("What would you like to modify? To modify DOB, please type 1, if you would like to modify your social security, type 2, if you would like to modify your pin, please type 3. Enter numerical value here: ")
        if modifyaccount == 1:
            #modifies their DOB
            dobmod = input("What would you like your new DOB to be? Please enter numerical value like so - dd/mm/yyyy. Enter here: ")
            newaccountinformation = ("INSERT INTO newaccountinformation (dob) values (dobmod)")
        if modifyaccount == 2:
            #modifies their SS
            ssmod = input("What would you like your new Social Security number to be? Please input in a xxx-xx-xxxx manner. Enter here: ")
            newaccountinformation = ("INSERT INTO newaccountinformation (ss) values (ssmod)")
        if modifyaccount == 3:
            #modifies their pin
            pinmod = input("What would you like your new pin to be? Enter here: ")
            newaccountinformation = ("INSERT INTO newaccountinformation (pin) values (pinmod)")
        

def checkbalance():
    #tells them their current account balance 
    print("You currently have a balance of {accbalance}")
    #would they like to deposit or withdraw money
    depositwithdrawquestion = input("Would you like to deposit or withdraw money?")
    if (depositwithdrawquestion == "Withdraw" or "withdraw"):
        #if they choose withdraw, their value is taken from their account balance, subtracted by how much they wish to withdraw, and then put back into the data set. 
        moneywithdrawn = input("How much would you like to withdraw?")
        newbalance = accbalance - moneywithdrawn
        print("You have {newbalance} left in your account!")
        insertbalance = ("INSERT INTO coolbank.balancesheet VALUES (newbalance)")

    elif (depositwithdrawquestion == "deposit" or "Deposit"):
        #similar to the withdraw question, but instead adds money and brings it back. 
        moneydeposited = input("How much would you like to deposit")
        newbalance = accbalance + moneydeposited
        print("You now have {newbalance}")
        insertbalance = ("INSERT INTO coolbank.balancesheet VALUES (newbalance)")
    else:
        print("Sorry, the item you've selected is not a part of our program. Plesae try again.")


if accnumber == accnumberinput and pinnumber == pinnumberinput:
    print("You have successfully logged in. Thank you for shopping with us.")
    services = input("What would you like to do? Would you like to look through our banking options or our account options? Type 1 for banking and 2 for account. Enter here:")
    # this simply goes through their two options. They can either check their monetary balance, or change their account. 
    if int(services) == 1:
        checkbalance()
    elif int(services) == 2:
        accountchanges()
else:
    print("Please try again.")







cursor.execute(accnumber)
cursor.execute(pinnumber)


for row in cursor:
    print(row)

for row in cursor:
    print(row)


connection.commit()

cursor.close()
connection.close()