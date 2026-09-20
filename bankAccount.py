class BankAccount:
    
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.card = None
        
    def deposit(self, amount):
        
        if amount <= 0:
            return "Amount must be greater than 0"
        
        self.balance += amount
        return f"New balance: {self.balance}"
    
    def withdraw(self, amount):

        if amount <= 0:
            return "Amount must be greater than 0"

        if amount > self.balance:
            return f"Insufficient balance! Current balance: {self.balance}"

        self.balance -= amount
        return f"Money was withdrawn. Residual balance: {self.balance}"
        
    def display_balance(self):
        
        return f"Current balance: {self.balance}"