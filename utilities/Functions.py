from datetime import datetime
from time import sleep

def title(tex,tam):
    print('-'*tam)
    print(tex.center(tam))
    print('-'*tam)

def deposit(txt="", limit=1500):
    while True:
        try:
            while True:
                d = float(input(txt))
                if d > limit:
                    print(f"You can only make deposits up to ${limit:.2f}")
                    sleep(1)
                elif d < 0.01:
                    print(f"You can only make deposits below $ 0.01")
                    sleep(1)
                else:
                    break
        except ValueError:
            print("Enter a valid number")
        else:
            now = datetime.now()
            format_now = now.strftime("%d/%m/%Y %I:%M:%S %p")
            dep = f"You deposited ${d:.2f} {format_now}\n"
            print(dep)
            sleep(1.5)
            return d,dep

def withdrawal(txt="",limit=500.00, balance=0):

    while True:
        try:
            while True:
                w = float(input(txt))
                if w > balance:
                    print("This amount exceeds your balance")
                elif w > limit:
                    print("You have exceeded your withdrawal limit")
                elif w < 0.01:
                    print("This amount is less than 0.01")
                else:
                    break
        except ValueError:
            print("Enter a valid number")
        else:
            now = datetime.now()
            format_now=now.strftime("%d/%m/%Y %I:%M:%S %p")
            a=f"You withdrew ${w:.2f} {format_now}\n"
            print(a)
            sleep(1.5)
            return w,a

def quest(tex="",y="Y",n="N"):
    while True:
        try:
            q=input(f"{tex} ({y}/{n}): ").strip().upper()[0]
        except:
            q=0
        if q == "Y":
            return y
        elif q == "N":
            return n
        else:
            print("Enter a valid option")
def balance_status(b):
    print(f"Your balance : $ {b:.2f}".center(50))
    print("-"*50)






