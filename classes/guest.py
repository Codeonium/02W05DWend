class Guest:
    def __init__(self, name, money, favourite_song):
        self.name = name
        self.money = money
        self.fav_song = favourite_song


    def pay_entry_fee(self, fee):
        self.money -= fee
    
    def cheer_to_music(self, music):
        #if fav_song == music:
        #return f"You know this music? this is {fav_song}, Woop, Woop"
        pass

    def pick_room_by_music(self, music):
        pass

    def pick_a_room_by_decade(self, room):
        pass
    
    def buy_a_drink(self, room ,drink):
        pass
    
    def pay_to_leave(self, fee):
        if self.money < fee:
            return f"Better start washing Mics"
        else:
            self.money -= fee
            return f"Best Mic night in ages"
    
    def become_a_member(self):
        pass

    def is_it_time_to_leave(self, time_in, money):
        #if many musics played... if money almost gone...
        pass
    