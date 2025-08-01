from utilities import *
bank=('''
[D] Deposit
[W] withdrawal
[E] Extract
[X] Exit

To select any option => ''')

balance=0
limit_withdrawal=500.00
extract=""
withdrawal_number=0
WITHDRAWAL_LIMIT=3
option=0
result_num=result_txt=0
while True:
    title("WELCOME TO THE IURY'S BANK", 50)
    balance_status(balance)
    try:
        option=input(bank).strip().upper()[0]
    except:
        option=0
    if option=="D":
        title("DEPOSIT AREA", 50)
        balance_status(balance)
        p = quest(f"Would you like to deposit")
        if p == "Y":
            result_num,result_txt=deposit("Enter your deposit amount: $ ")
            balance+=result_num
            extract+=result_txt
    elif option=="W":
        title("WITHDRAWAL AREA", 50)
        balance_status(balance)
        print(f"Withdrawal limit is ${limit_withdrawal:.2f}, {WITHDRAWAL_LIMIT} times per day")
        p=quest(f"Would you like to withdrawal")
        if p == "Y":
            if withdrawal_number <= 3:
                result_num,result_txt =withdrawal("Enter your withdrawal amount: $ ",500.00,balance)
                balance-=result_num
                extract+=result_txt
                withdrawal_number+=1
            else:
                print("You have exceeded your daily withdrawal limit")
    elif option=="E":
        title("EXTRACT", 50)
        print(f"Your Extract is here:\n0{extract}")
        while True:
            p=input("press enter to go back: ")
            if p == "":
                break

    elif option=="X":
        title("GODBYE, SEE YOU LATER...", 50)
        break
    else:
        print("Please enter a valid option")
        sleep(1.5)
