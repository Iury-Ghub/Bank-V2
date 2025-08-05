from utilities.Functions import *
from time import sleep


def main():
    bank = ('[D] Deposit\n'
            '[W] withdrawal\n'
            '[E] Extract\n'
            '[Na] New Account\n'
            '[La] List Account\n'
            '[Nu] New User\n'
            '[Q] Quit\n'
            'To select any option => ')

    WITHDRAWAL_LIMIT = 3
    AGENCY="0001"

    limit_withdrawal = 500.00
    deposit_limit = 1500.00
    balance = 0
    withdrawal_number = 0
    account_number = 1
    extract_list = list()
    users=[]
    accounts=[]

    while True:
        title("WELCOME TO THE IURY'S BANK", 50)
        balance_status(balance)
        option=input(bank).strip().upper()

        if option == "D":
            title("DEPOSIT AREA", 50)
            balance_status(balance)
            p = quest(f"Would you like to deposit")
            if p == "Y":
                print("~"*50)
                print(f"Deposit limit is $ {deposit_limit:.2f}")
                print("~"*50)
                balance,extract=deposit(balance,deposit_limit)
                sleep(1.5)
                extract_list.append(extract)

        elif option == "W":
            title("WITHDRAWAL AREA", 50)
            balance_status(balance)
            p = quest(f"Would you like to withdrawal")
            if p == "Y":
                print("~"*50)
                print(f"Withdrawal limit is ${limit_withdrawal:.2f}, {WITHDRAWAL_LIMIT} times per day")
                balance,extract=withdrawal("Enter the withdrawal amount: $ ", balance, limit_withdrawal, withdrawal_number, WITHDRAWAL_LIMIT)
                sleep(1.5)
                if withdrawal_number <= 3:
                    withdrawal_number+=1
                    extract_list.append(extract)

        elif option == "E":
            title("EXTRACT", 50)
            show_extract(extract_list)
            while True:
                p=input("press enter to go back: ")
                if p == "":
                    break

        elif option == "NA":
            account = new_account(AGENCY, account_number, users)
            if account:
                account_number+=1
                accounts.append(account)
            sleep(1.5)
        elif option == "LA":
            list_accounts(accounts)
        elif option == "NU":
            new_user(users)
        elif option == "Q":
            title("GODBYE, SEE YOU LATER...", 50)
            break
        else:
            print("Please enter a valid option")
            sleep(1.5)
main()