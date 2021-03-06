import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.dior = Guest("Dior", 200, "My heart will go on") # the self is a sugar for Guest
        self.frodo = Guest("Frodo", 10, "The road goes on... and on...")

    def test_guest_has_name(self):
        self.assertEqual("Dior", self.dior.name)

    def test_guest_has_money(self):
        self.assertEqual(200, self.dior.money)

    def test_guest_has_fav_song(self):
        self.assertEqual("My heart will go on", self.dior.fav_song)

    def test_guest_can_pay(self):
        self.dior.pay_entry_fee(20)
        self.assertEqual(180, self.dior.money)

    def test_pay_to_leave(self):
        frodo_poor = self.frodo.pay_to_leave(20)
        dior_loaded = self.dior.pay_to_leave(20)
        self.assertEqual("Better start washing Mics", frodo_poor)
        self.assertEqual(("Best Mic night in ages", 180), (dior_loaded, self.dior.money))
    
    