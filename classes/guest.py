class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def pay_entry_fee(self, fee):
        self.money -= fee
        