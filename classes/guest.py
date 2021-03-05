class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def pay_entry_fee(self, fee):
        self.money -= fee
    
    def pay_to_leave(self, fee):
        if self.money < fee:
            return f"Better start washing Mics"
        else:
            self.money -= fee
            return f"Best Mic night in ages"

    