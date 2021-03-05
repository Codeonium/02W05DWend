import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.dior = Guest("myself", 200) # the self is a sugar for Guest

    def test_guest_can_pay(self):
        self.dior.pay_entry_fee(20)
        self.assertEqual(180, self.dior.money)