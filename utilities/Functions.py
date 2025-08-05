from datetime import datetime
from time import sleep

def title(tex,tam):
    print('-'*tam)
    print(tex.center(tam))
    print('-'*tam)

def quest(tex="", y="Y", n="N"):
    while True:
        q = input(f"{tex} ({y}/{n}): ").strip().upper()
        if q == "Y":
            return y
        elif q == "N":
            return n
        else:
            print("Enter a valid option")

def balance_status(b):
    print(f"Your balance : $ {b:.2f}".center(50))
    print("-"*50)

def deposit(balance, deposit_limit):
    while True:
        try:
            value=float(input("Enter the amount to deposit: $ "))
            while True:
                if value > deposit_limit:
                    print(f"You can only make deposits up to ${deposit_limit:.2f}")
                    break

                elif value < 0.01:
                    print(f"You can only make deposits below $ 0.01")
                    break

                else:
                    balance += value
                    now = datetime.now()
                    format_now = now.strftime("%d/%m/%Y %I:%M:%S %p")
                    txt = f"You deposited ${value:.2f} {format_now}"
                    print(txt)
                    return balance, txt
        except:
            print("Please enter a valid number")




def withdrawal(txt, balance, limit_withdrawal, withdrawal_number, WIHDRAWAL_LIMIT,):
        while True:
            try:
                value=float(input(txt))
                while True:
                    if value > balance:
                        print("This amount exceeds your balance")
                        break

                    elif value > limit_withdrawal:
                        print("You have exceeded your withdrawal limit")
                        break

                    elif value < 0.01:
                        print("This amount is less than 0.01")
                        break

                    elif withdrawal_number >= WIHDRAWAL_LIMIT:
                        print("You have exceeded your withdrawal number limit")
                        return balance, None
                    else:
                        balance -= value
                        now = datetime.now()
                        format_now = now.strftime("%d/%m/%Y %I:%M:%S %p")
                        extract = f"You withdrew ${balance:.2f} {format_now}"
                        print(extract)
                        return balance, extract
            except :
                print("Enter a valid number")


def show_extract(extract_list):
    print("#"*50)
    print(f"Your Extract is here: ")
    for l in extract_list:
        print(l)
    print("#"*50)


def new_user(users):
    id_user=input("Enter your ID: ")
    user=user_filter(id_user,users)
    if user != 0:
        print("This user already exists.")
        sleep(1.5)
        return
    name=input("Enter your name: ")
    birthdate=input("Enter your birthdate: ")
    address={"Street Address": input("Enter your street address: "),
             "House Number": input("Enter your house number: "),
             "Neighborhood": input("Enter your neighborhood: "),
             "City": input("Enter your city: "),
             "State abbreviation": input("Enter your state: ")}
    users.append({'Name': name, 'Birthdate': birthdate, 'ID': id_user, 'Address': address})
    print("~"*50)
    print("Registration successful...")
    print("~" * 50)


def user_filter(id, users):
    filtered_users=[user for user in users if user["ID"] == id]
    return filtered_users[0] if filtered_users else 0

def new_account(agency, account_number, users):
    id=input("Enter your ID: ")
    user=user_filter(id,users)
    if user != 0:
        print("Account created successfully...")
        return {"Agency":agency, "Account_Number":account_number, "User":user}

    print("\nUser not found, quit in 3...2...1...")

def list_accounts(acconts):
    for accont in acconts:
        linha=(f"Agency: {accont['Agency']}\n"
               f"Account Number: {accont['Account_Number']}\n"
               f"Account Holder: {accont['User']['Name']}")
        print("=" * 50)
        print(linha)
        print("="*50)
