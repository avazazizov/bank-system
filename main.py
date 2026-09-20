import msvcrt
import os
from bank import Bank

bank = Bank()

options = [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Transfer",
    "Check Balance",
    "Show Card",
    "Show All Accounts",
    "Delete Card",
    "Delete Account",
    "Exit"
]

selected = 0

while True:

    os.system("cls")

    print("===== BANK SYSTEM =====\n")

    for i, option in enumerate(options):

        if i == selected:
            print(f"> {option}")
        else:
            print(f"  {option}")

    key = msvcrt.getch()

    if key == b'\xe0':

        key = msvcrt.getch()

        if key == b'H':
            selected -= 1

        elif key == b'P':
            selected += 1

    if selected < 0:
        selected = len(options) - 1

    elif selected >= len(options):
        selected = 0

    elif key == b'\r':

        if selected == 0:
            bank.create_account()

        elif selected == 1:
            bank.deposit()

        elif selected == 2:
            bank.withdraw()

        elif selected == 3:
            bank.transfer()

        elif selected == 4:
            bank.check_balance()

        elif selected == 5:
            bank.show_card()

        elif selected == 6:
            bank.show_all_accounts()

        elif selected == 7:
            bank.delete_card()

        elif selected == 8:
            bank.delete_account()

        elif selected == 9:
            print("Goodbye!")
            break

        input("\nPress Enter to continue...")
        
