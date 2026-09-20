import json

from customer import Customer
from bankAccount import BankAccount
from bankCard import BankCard

class Bank:
    
    def __init__(self):
        self.accounts = []
        self.next_account_number = 1001
        self.next_customer_id = 1
        
        self.load_data()
        
    def create_account(self):
        
        name = input("Enter name: ")
        balance = float(input("Enter initial balance: "))
        
        customer = Customer(name, self.next_customer_id)
        
        account = BankAccount(
            self.next_account_number,
            customer,
            balance
        )
        
        self.accounts.append(account)

        print("Account created successfully!")
        print(f"Account number: {self.next_account_number}")
        
        choice = input("Do you want to create a bank card? (yes/no): ").lower()
        
        if choice == "yes":
            account.card = BankCard()
            
            print("Bank card created successfully!")
            print(f"Card Number: {account.card.card_number}")
            print(f"Expiration Date: {account.card.expiration_date}")
            print(f"CVV: {account.card.cvv}")
            
        else:
            print("Account created without a bank card.")

        self.next_account_number += 1
        self.next_customer_id += 1

        self.save_data()
        
    def save_data(self):
        
        accounts_data = []
        
        for account in self.accounts:
            
            account_data = {
                "account_number": account.account_number,
                "customer_id": account.owner.customer_id,
                "name": account.owner.name,
                "balance": account.balance,
                "card": None
            }
            
            if account.card is not None:
                account_data["card"] = {
                    "card_number": account.card.card_number,
                    "expiration_date": account.card.expiration_date,
                    "cvv": account.card.cvv
                }
            
            accounts_data.append(account_data)
            
        data = {
            "next_account_number": self.next_account_number,
            "next_customer_id": self.next_customer_id,
            "accounts": accounts_data
        }
        
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        
    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        return None


    def find_account_by_card(self, card_number):

        for account in self.accounts:

            if account.card is not None:

                if account.card.card_number == card_number:
                    return account

        return None
        
    def deposit(self):
        
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount: "))
        
        account = self.find_account(account_number)
        
        if account is None:
            print("Account not found!")
            return
        
        print(account.deposit(amount))
        self.save_data()
        
    def withdraw(self):
        
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount: "))
        
        account = self.find_account(account_number)

        if account is None:
            print("Account not found!")
            return

        print(account.withdraw(amount))
        self.save_data()

    def transfer(self):

        from_card_number = input("Enter sender card number: ")
        to_card_number = input("Enter receiver card number: ")
        amount = float(input("Enter amount: "))

        from_account = self.find_account_by_card(from_card_number)
        to_account = self.find_account_by_card(to_card_number)

        if from_account is None:
            print("Sender card not found!")
            return

        if to_account is None:
            print("Receiver card not found!")
            return

        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        if amount > from_account.balance:
            print("Insufficient balance!")
            return

        from_account.balance -= amount
        to_account.balance += amount

        self.save_data()

        print("Transfer successful!")
               
    def check_balance(self):

        card_number = input("Enter card number: ")

        account = self.find_account_by_card(card_number)

        if account is None:
            print("Card not found!")
            return

        print(f"Card Number: {account.card.card_number}")
        print(f"Owner: {account.owner.name}")
        print(f"Current balance: {account.balance} AZN")   

    def show_all_accounts(self):

        if not self.accounts:
            print("No accounts found!")
            return

        for account in self.accounts:

            print(f"Account Number: {account.account_number}")
            print(f"Owner: {account.owner.name}")
            print(f"Balance: {account.balance} AZN")

            if account.card is not None:
                print(f"Card Number: {account.card.card_number}")
            else:
                print("Card: No card")

            print("--------------------")
       
    def delete_account(self):
        
        account_number = int(input("Enter account number: "))
        
        account = self.find_account(account_number)
        
        if account is None:
            print("Account not found!")
            return
        
        self.accounts.remove(account)
        self.save_data()
        print("Account deleted successfully!")
        
    def delete_card(self):
        
        card_number = input("Enter card number: ")
        
        account = self.find_account_by_card(card_number)
        
        if account is None:
            print("Card not found!")
            return
        
        account.card = None
        
        self.save_data()
        print("Card deleted successfully!")
        
    def load_data(self):

        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return

        self.next_account_number = data["next_account_number"]
        self.next_customer_id = data["next_customer_id"]

        for account_data in data["accounts"]:

            customer = Customer(
                account_data["name"],
                account_data["customer_id"]
            )

            account = BankAccount(
                account_data["account_number"],
                customer,
                account_data["balance"]
            )

            if account_data["card"] is not None:

                card_data = account_data["card"]

                card = BankCard()

                card.card_number = card_data["card_number"]
                card.expiration_date = card_data["expiration_date"]
                card.cvv = card_data["cvv"]

                account.card = card

            self.accounts.append(account)
                    
    def show_card(self):

        card_number = input("Enter card number: ")

        account = self.find_account_by_card(card_number)

        if account is None:
            print("Card not found!")
            return

        print(f"Owner: {account.owner.name}")
        print(f"Card Number: {account.card.card_number}")
        print(f"Expiration Date: {account.card.expiration_date}")
        print(f"CVV: {account.card.cvv}")