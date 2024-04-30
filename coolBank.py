import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'coolbank', password = 'Basketballrocks123')

cursor = connection.cursor()

accnumber = ('SELECT customeraccnumber FROM coolbank.customerinformation')

pinnumber = ('SELECT customerpin FROM coolbank.customerinformation')

accbalance = ('SELECT customerbalance FROM coolbank.balancesheet')

accnumberinput = input("What is your account number: ")
pinnumberinput = input("What is your pin number: ")

customeraccount = ('SELECT accountinformation FROM coolbank.customeraccount')

if accnumber == accnumberinput and pinnumber == pinnumberinput:
    print("You have successfully logged in. Thank you for shopping with us.")
    services = input("What would you like to do? Would you like to look through our banking options or our account options? Type 1 for banking and 2 for account. Enter here:")
    if int(services) == 1:
        checkbalance()
    elif int(services) == 2:
        accountchanges()
else:


def accountchanges():
    accountquestion  = input("Welcome to our account services. What would you like to do? To create a new account, type 1, to discontinue an account or permanently delete it, type 2, and or to change information, type 3. Enter numerical value here:")
    if accountquestion == 1:
        DOBacc = (input("What is your DOB? Enter in a 00/00/0000 value"))
        SSacc =  (input("What is your social security number? Enter as a 000-00-0000"))
        PINacc = (input("What would you like your account pin to be? Enter a three digit pin:"))
        newaccountinformation = ("INSERT INTO newaccountinformation (dob, ss, pin) VALUES (DOBacc, SSacc, PINacc)")
    elif accountquestion == 2:
        accountNumber = input("Please confirm your account number. Enter here:")
        pinNumber = input("Please confirm your pin number. Enter here")
        if accountNumber == accnumberinput:
            confirmation = input("Are you sure you wish to delete your account?")
            if confirmation == "Yes" or 'yes':
                accnumberinput = ("DELETE accountinformation FROM coolbank")
                print("You have deleted your account with CoolBank. We wish you a good day.")
    elif accountquestion == 3:
        modifyaccount = input("What would you like to modify? To modify DOB, please type 1, if you would like to modify your social security, type 2, if you would like to modify your pin, please type 3. Enter numerical value here: ")
        if modifyaccount == 1:
            dobmod = input("What would you like your new DOB to be? Please enter numerical value like so - dd/mm/yyyy. Enter here: ")
            newaccountinformation = ("INSERT INTO newaccountinformation (dob) values (dobmod)")
        if modifyaccount == 2:
            ssmod = input("What would you like your new Social Security number to be? Please input in a xxx-xx-xxxx manner. Enter here: ")
            newaccountinformation = ("INSERT INTO newaccountinformation (ss) values (ssmod)")
        if modifyaccount == 3:
            pinmod = input("What would you like your new pin to be? Enter here: ")
            newaccountinformation = ("INSERT INTO newaccountinformation (pin) values (pinmod)")
            


            




def checkbalance():
    print("You currently have a balance of {accbalance}")
    depositwithdrawquestion = input("Would you like to deposit or withdraw money?")
    if (depositwithdrawquestion == "Withdraw" or "withdraw"):
        moneywithdrawn = input("How much would you like to withdraw?")
        newbalance = accbalance - moneywithdrawn
        print("You have {newbalance} left in your account!")
        insertbalance = ("INSERT INTO coolbank.balancesheet VALUES (newbalance)")

    elif (depositwithdrawquestion == "deposit" or "Deposit"):
        moneydeposited = input("How much would you like to deposit")
        newbalance = accbalance + moneydeposited
        print("You now have {newbalance}")
        insertbalance = ("INSERT INTO coolbank.balancesheet VALUES (newbalance)")
    else:
        print("Sorry, the item you've selected is not a part of our program. Plesae try again.")













cursor.execute(accnumber)
cursor.execute(pinnumber)


for row in cursor:
    print(row)

for row in cursor:
    print(row)


connection.commit()

cursor.close()
connection.close()