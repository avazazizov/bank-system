import random
from datetime import datetime, timedelta


class BankCard:

    def __init__(self):
        first_8 = "41697388"

        last_8 = ''.join(str(random.randint(0, 9)) for _ in range(8))

        self.card_number = first_8 + last_8

        expiration = datetime.now() + timedelta(days=5 * 365)
        self.expiration_date = expiration.strftime("%m/%y")

        self.cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))