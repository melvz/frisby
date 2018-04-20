
from bank_account import Account
ACCOUNTS = {}

show_menu = True

while(show_menu):
        print "1 - CREATE account"
        print "2 - VIEW accounts"
        print "3 - WITHDRAWAL"
        print "4 - EXIT"


        selection = raw_input("Select Action:  ")

        if selection == "1":
                name = raw_input("Enter Name:  ")
                balance = raw_input("Indicate initial balance amount:  ")

                account = Account(name=name, balance=float(balance), number=str(len(ACCOUNTS) + 1))
                ACCOUNTS[account.number] = account
                print "Account Created =) "

        elif selection == "2":
                for account_no, account in ACCOUNTS.items():
                        print "Account Number: %s; Account Name: %s; Is Open?: %s; Date Opened: %s; Balance: %s" % (account_no, account.name, account.is_open, account.date_opened, account.balance)

        if selection == "3":
                print "Time to WITHDRAW your cash"
                withdraw_acct = raw_input("Accountnumber: ")
                for withdraw_acct, account in ACCOUNTS.items():
                        withdrawal_amount = float(raw_input("key in the cash amount you want spill out from this Machine---> :    "))

                        if withdrawal_amount < account.balance:
                                account.balance -=withdrawal_amount
                                print "your new balance is ", account.balance
                        else:
                                print "No sufficient funds"




        elif selection == "4":
                show_menu = False
                print "Exit"

        else:
                print "Please try again and select valid option"

## end of code
